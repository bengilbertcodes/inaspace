from django.urls import path
from bookings.views import BookingView, BookingSuccessView

urlpatterns = [
    path('bookings/', BookingView.as_view(), name='booking'),
    path('booking_success/', BookingSuccessView.as_view(), name='booking_success'),
]

