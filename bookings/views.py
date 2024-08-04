from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Booking
from .forms import BookingForm


class BookingView(LoginRequiredMixin, generic.FormView):
    """
    A view for handling the booking form submission.
    Requires user to be logged in and associates booking with the current user
    """
    template_name = 'bookings/booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking_success')

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class BookingSuccessView(generic.TemplateView):
    """
    A view for handling the succesful booking confirmation screen
    """
    template_name = 'bookings/booking_success.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                        generic.DeleteView):
    """
    A view to handle deleting an existing booking.
    """
    model = Booking
    success_url = reverse_lazy('home')
    template_name = 'bookings/booking_confirm_delete.html'

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        self.add_success_message()
        return response

    def add_success_message(self):
        messages.success(self.request, 'Booking successfully deleted.')


class BookingEditView(LoginRequiredMixin, UserPassesTestMixin,
                      generic.UpdateView):
    """
    A view to handle Editing an existing booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def form_valid(self, form):
        messages.success(
            self.request, 'Booking has been successfully updated.')
        return super().form_valid(form)
