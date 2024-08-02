from django.contrib import admin
from .models import Booking, Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'capacity', 'is_available', 'room_type')
    list_filter = ('room_type', 'is_available')
    search_fields = ('room_number',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_time', 'end_time', 'created_at')
    list_filter = ('room', 'start_time', 'end_time')
    search_fields = ('user__username', 'room__room_number')
