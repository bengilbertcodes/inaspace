from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from bookings.forms import CustomSignupForm, BookingForm
from .models import Booking, ROOM_TYPE, Room
from django.contrib.auth.models import User


class TestSignupForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields """
        form = CustomSignupForm({
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertTrue(form.is_valid(), msg='Form is not valid')

    def test_form_missing_email(self):
        """ Test for missing email """
        form = CustomSignupForm({
            'username': 'testuser',
            'email': '',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertFalse(form.is_valid(), msg='Form is valid')

    def test_form_missing_password1(self):
        """ Test for missing password1 """
        form = CustomSignupForm({
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': '',
            'password2': 'ComplexPass123!',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertFalse(form.is_valid(), msg='Form is valid')

    def test_form_missing_password2(self):
        """ Test for missing password2 """
        form = CustomSignupForm({
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': '',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertFalse(form.is_valid(), msg='Form is valid')

    def test_form_missing_username(self):
        """ Test for missing username """
        form = CustomSignupForm({
            'username': '',
            'email': 'testuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertFalse(form.is_valid(), msg='Form is valid')

    def test_form_incorrect_email(self):
        """ Test for incorrect email format """
        form = CustomSignupForm({
            'username': 'testuser',
            'email': 'bobatdotcom',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertFalse(form.is_valid(), msg='Form is valid')

    def test_form_password_mismatch(self):
        """ Test for password mismatch """
        form = CustomSignupForm({
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'DifferentPass123!',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertFalse(form.is_valid(), msg='Form is valid')


class testBookingForm(TestCase):

    def setUp(self):
        """ Sets up a test user """
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.room_type = Room.objects.create(
            room_number='101', capacity=10, room_type='office')

    def test_form_date_not_in_past(self):
        """ Test for date not being before now (today) """
        past_date = timezone.now().date() - timedelta(days=1)
        form_data = {
            'room': self.room_type,
            'date': past_date,
            'start_time': '10:00',
            'end_time': '11:00',
        }
        form = BookingForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid(), msg='Form is valid')

    def test_form_start_time_not_in_past(self):
        """ Test to ensure start_time cannot be in the past """
        past_datetime = timezone.now() - timedelta(minutes=10)
        form_data = {
            'room': self.room_type,
            'date': past_datetime.date(),
            'start_time': past_datetime.time(),
            'end_time': (past_datetime + timedelta(hours=1)).time(),
        }
        form = BookingForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid(), msg='Form is valid')

    def test_end_time_after_start_time(self):
        """ Test for end_time not before start_time """
        future_date = timezone.now().date() + timedelta(days=1)
        form_data = {
            'room': self.room_type,
            'date': future_date,
            'start_time': '12:00',
            'end_time': '11:00',
        }
        form = BookingForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid(), msg='Form is valid')

    def test_valid_booking(self):
        future_date = timezone.now().date() + timedelta(days=1)
        form_data = {
            'room': self.room_type,
            'date': future_date,
            'start_time': '14:00',
            'end_time': '16:15',
        }
        form = BookingForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid(), msg='Form is invalid')
