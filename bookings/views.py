from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Booking
from .forms import BookingForm


class BookingView(LoginRequiredMixin, generic.FormView):
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
    template_name = 'bookings/booking_success.html'


class BookingDeleteView(LoginRequiredMixin, generic.View):
    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, booking_id=booking_id)
        return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})

    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, booking_id=booking_id)
        booking.delete()
        messages.success(request, 'Your booking has been successfully deleted')
        return redirect(reverse_lazy('home'))


class BookingEditView(LoginRequiredMixin, generic.View):
    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
        form = BookingForm(instance=booking)
        return render(request, 'bookings/booking_form.html', {'form': form})
    
    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(
            Booking, booking_id=booking_id, user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking has been successfully updated.')
            return redirect(reverse_lazy('home'))
        return render(request, 'bookings/booking_form.html', {'form': form})
