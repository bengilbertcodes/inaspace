from django.urls import path
from bookings.views import BookingView, BookingSuccessView, BookingDeleteView

urlpatterns = [
    path('bookings/', BookingView.as_view(), name='booking'),
    path('booking_success/', BookingSuccessView.as_view(), name='booking_success'),
    path('delete/<int:booking_id>/', BookingDeleteView.as_view(), name='delete_booking'),
]

