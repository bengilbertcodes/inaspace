from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import datetime, timedelta, time


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=25, required=False, label='First Name')
    last_name = forms.CharField(
        max_length=25, required=False, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                # Ensure date cannot be in the past
                'min': datetime.now().date().strftime('%Y-%m-%d')
            }),
            'start_time': forms.TextInput(attrs={
                'class': 'form-control',
                'step': 900,  # 15 minutes
                'type': 'text',
                'placeholder': 'HH:MM'
            }),
            'end_time': forms.TextInput(attrs={
                'class': 'form-control',
                'step': 900,  # 15 minutes
                'type': 'text',
                'placeholder': 'HH:MM'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.is_editing = self.instance.pk is not None

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        room = cleaned_data.get('room')
        booking_id = self.instance.pk if self.instance else None

        # Combine date and time to datetime objects
        if date and start_time:
            start_datetime = datetime.combine(date, start_time)
        else:
            start_datetime = None

        if date and end_time:
            end_datetime = datetime.combine(date, end_time)
        else:
            end_datetime = None

        # Ensure datetime is in the future
        if start_datetime and start_datetime < datetime.now():
            raise ValidationError('Start time cannot be in the past.')

        if end_datetime and end_datetime < datetime.now():
            raise ValidationError('End time cannot be in the past.')

        # Update end_time based on start_time if creating a new booking
        if not self.is_editing and start_datetime and not end_datetime:
            end_datetime = start_datetime + timedelta(hours=1)
            cleaned_data['end_time'] = end_datetime.time()

        # Validate if start_datetime and end_datetime are provided and valid
        if start_datetime and end_datetime:
            if end_datetime <= start_datetime:
                raise ValidationError('End time must be after start time.')

            # Check for overlapping bookings,
            # When editing, exclude the current booking
            overlapping_bookings = Booking.objects.filter(
                room=room,
                start_time__lt=end_datetime,
                end_time__gt=start_datetime
            ).exclude(pk=booking_id)

            if overlapping_bookings.exists():
                raise ValidationError(
                    'This room is already booked during this time.')

        return cleaned_data
