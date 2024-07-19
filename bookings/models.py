from django.db import models
from django.contrib.auth.models import User

class RoomType(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=50)

class Room(models.Model):
	name = models.IntegerField
	room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	capacity = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.name} ({self.room_type.name}) - {self.location} - Capacity: {self.capacity}"


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"

class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	date = models.DateField
	time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('room', 'date', 'time_slot')
	
	def __str__(self):
		return f"{self.user} booked {self.room} on {self.date} from {self.time_slot}"
