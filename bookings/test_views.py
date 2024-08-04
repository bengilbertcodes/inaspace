from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from bookings.models import Booking, Room


# Create your tests here.
class BookingViewTest(TestCase):
	def setUp(self):
		# Create a test room
		self.room = Room.objects.create(
			room_number='101',
			capacity=10,
			is_available=True,
			room_type='office'
		)
		# Create a test user
		self.user = User.objects.create_user(username='testuser',
									   password='testpassword')
		now = timezone.now()
		# Create a test booking
		self.booking = Booking.objects.create(
			user=self.user,
			room=self.room,
			date=now.date(),
			start_time='10:00',
			end_time='12:30',
		)
		self.url = reverse('booking')

	def test_booking_view_authenticated(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'bookings/booking_form.html')

	def test_booking_view_post(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.post(self.url, {
			'room': self.room.room_id,
			'date': timezone.now().date(),
			'start_time': '10:00',
			'end_time': '12:30'
		})
		self.assertEqual(response.status_code, 200)
		self.assertTrue(Booking.objects.filter(user=self.user).exists())

class BookingSuccessViewTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser',
                                      password='testpassword')
		self.url = reverse('booking_success')

	def test_booking_success_view(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)


class BookingDeleteViewTest(TestCase):
    def setUp(self):
        # Create a test user and booking
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.room = Room.objects.create(
            room_number='101',
            capacity=10,
            is_available=True,
            room_type='office'
        )
        self.booking = Booking.objects.create(
            user=self.user,
            room=self.room,
            date=timezone.now().date(),
            start_time='11:30',
            end_time='13:00'
        )
        # URL for the delete view
        self.url = reverse('delete_booking', kwargs={'pk': self.booking.pk})

    def test_booking_delete_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Booking.objects.filter(pk=self.booking.pk).exists())

class BookingEditViewTest(TestCase):
    def setUp(self):
        # Create a test user and booking
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.room = Room.objects.create(
            room_number='101',
            capacity=10,
            is_available=True,
            room_type='office'
        )
        self.booking = Booking.objects.create(
            user=self.user,
            room=self.room,
            date=timezone.now().date(),
            start_time=timezone.now().time(),
            end_time=(timezone.now() + timezone.timedelta(hours=1)).time()
        )
        # URL for the edit view
        self.url = reverse('edit_booking', kwargs={'pk': self.booking.pk})

    def test_booking_edit_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_form.html')
