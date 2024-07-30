from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

ROOM_TYPE = [
    ('office', 'Office'),
    ('meeting', 'Meeting'),
    ('rehearsal', 'Rehearsal'),
]


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPE,
        default='office'
    )

    def __str__(self):
        return f"({self.room_number}) - {self.get_room_type_display()}"


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        # prevents overlapping bookings
        unique_together = ('room', 'start_time', 'end_time')

    def __str__(self):
        username = self.user.username
        room_number = self.room.room_number
        start_time_str = self.start_time.strftime('%d-%m-%Y %H:%M:%S')
        end_time_str = self.end_time.strftime('%H:%M:%S')
        booking_description = (
            f"Booking by {username} "
            f"for {room_number} "
            f"from {start_time_str} "
            f"to {end_time_str}"
        )
        return booking_description
