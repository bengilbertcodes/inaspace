from django.urls import path, include
from . import views

urlpatterns = [
    path('bookings/', views.booking_view, name='booking'),
]

