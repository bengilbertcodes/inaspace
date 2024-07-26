from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Booking
from .forms import BookingRequestForm


def booking_request(request):
    form_class = BookingRequestForm
    template_name = 'booking/booking_request.html'
    model = Booking


