from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
	ROOM_TYPE = [
		('office', 'Office'),
		('meeting', 'Meeting'),
		('rehearsal', 'Rehearsal'),
	]

	room_number = models.Charfield(max_length=10, unique=True)
	capacity = models.PositiveIntegerField()
	is_available = models.BooleanField(default=True)
	room_type = models.CharField(
		max_length=20,
		choices=ROOM_TYPE,
		default='office'
		)
	
	def __str__(self):
		return f"{self.room_name} ({self.room_number}) - {self.get_room_type_display()}"

class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	created_at = models.DateTimeField(default=timezone.now)

	class Meta:
		unique_together = ('room', 'start_time', 'end_time') # prevents overlapping bookings
	
	def __str__(self):
    # Extract user and room details
		username = self.user.username
		room_name = self.room.room_name
    
    # Format the booking time range
		start_time_str = self.start_time.strftime('%d-%m-%Y %H:%M:%S')
		end_time_str = self.end_time.strftime('%d-%m-%Y %H:%M:%S')
    
    # Construct the string representation
		booking_description = (
			f"Booking by {username} "
			f"for {room_name} "
			f"from {start_time_str} "
			f"to {end_time_str}"
		)
    
		return booking_description