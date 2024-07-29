from django.urls import path, include
from bookings.views import BookingView

urlpatterns = [
    path('bookings/', BookingView.as_view(), name='booking'),
]

