from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from django.contrib.auth.models import User
from datetime import timedelta


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        room = cleaned_data.get('room')
        booking_id = self.instance.booking_id

        # Ensure end_time is one hour after start_time by default if not provided
        if start_time and not end_time:
            end_time = start_time + timedelta(hours=1)
            cleaned_data['end_time'] = end_time

        # Validate if start_time and end_time are provided and valid
        if start_time and end_time:
            if end_time <= start_time:
                raise ValidationError('End time must be after start time.')

            # Check for overlapping bookings
            overlapping_bookings = Booking.objects.filter(
                room=room,
                start_time__lt=end_time,
                end_time__gt=start_time
            ).exclude(booking_id=booking_id)  # Exclude the current booking if editing

            if overlapping_bookings.exists():
                raise ValidationError(
                    'This room is already booked during this time.')

        return cleaned_data
