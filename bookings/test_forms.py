from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from bookings.forms import CustomSignupForm, BookingForm
from .models import Booking, ROOM_TYPE
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
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.room_type = ROOM_TYPE[0][0]
