from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ('user', 'room', 'start_time', 'end_time', 'created_at')
	list_filter = ('room', 'start_time', 'end_time')
	search_fields = ('user__username', 'room__room_name')
