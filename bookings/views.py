from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


@login_required
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return render(request, 'bookings/booking_success.html')
    else:
        form = BookingForm(user=request.user)
    return render(request, 'bookings/booking_form.html', {'form': form})
