from django.contrib import admin
from .models import RoomType, Room, TimeSlot, Booking

class RoomAdmin(admin.ModelAdmin):
	list_display = ('name', 'room_type', 'location', 'capacity')
	search_fields = ('name', 'location')
	list_filter = ('room_type',)

admin.site.register(RoomType)
admin.site.register(Room, RoomAdmin)
admin.site.register(TimeSlot)
admin.site.register(Booking)
