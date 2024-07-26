from django import forms
from django.core.exceptions import ValidationError
from .models import Booking, Room
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
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user
        if user:
            self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.filter(id=user.id),
                                                         widget=forms.HiddenInput())
        else:
            self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.none(),
                                                         widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        room = cleaned_data.get('room')

        # Ensure end_time is one hour after start_time by default if not provided
        if start_time and not end_time:
            end_time = start_time + timedelta(hours=1)
            cleaned_data['end_time'] = end_time

        # Check for overlapping bookings
        if room and start_time and end_time:
            overlapping_bookings = Booking.objects.filter(
                room=room,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            if overlapping_bookings.exists():
                raise ValidationError(
                    'This room is already booked during this time.')

        return cleaned_data
