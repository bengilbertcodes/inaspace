from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Booking

class BookingRequestForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = [
            'room_type', 'start_time', 'end_time'
		]
        labels = {
            'room_type': 'Room Type',
            'start_time': 'Start Time',
            'end_time': 'End Time',
		}
