from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Booking


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


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
