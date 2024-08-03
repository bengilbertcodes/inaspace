from django.urls import path
from bookings.views import (BookingView, BookingSuccessView,
BookingDeleteView, BookingEditView)

urlpatterns = [
    path('bookings/', BookingView.as_view(),name='booking'),
    path('booking_success/', BookingSuccessView.as_view(),
         name='booking_success'),
    path('delete/<int:pk>/', BookingDeleteView.as_view(),
         name='delete_booking'),
    path('booking/edit/<int:pk>/', BookingEditView.as_view(),
         name='edit_booking'),
]
