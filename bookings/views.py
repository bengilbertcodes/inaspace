from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Booking
from .forms import BookingForm


class BookingView(generic.FormView):
    template_name = 'bookings/booking_form.html'
    form_class = BookingForm
    success_url = 'bookings/booking_success.html'

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        return self.form_class(user=self.request.user)

class OpenBookingViews(generic.ListView):
    model = Booking
