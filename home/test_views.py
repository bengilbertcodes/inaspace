from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from bookings.models import Booking, Room


# Create your tests here.
class HomeViewTest(TestCase):
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
			start_time=now.time(),
			end_time=(now + timezone.timedelta(hours=1)).time(),
			date=now.date()
		)
		self.url = reverse('home')

	def test_home_view_authenticated(self):
		self.client.login(username='testuser', password='testpassword')
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		self.assertIn('bookings', response.context)
		self.assertEqual(len(response.context['bookings']), 1)
		self.assertEqual(response.context['bookings'][0], self.booking)

	def test_home_view_not_authenticated(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		self.assertIn('bookings', response.context)
		self.assertEqual(len(response.context['bookings']), 0)
