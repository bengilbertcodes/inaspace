from django.core.management.base import BaseCommand
from bookings.models import Room


class Command(BaseCommand):
    help = 'Populate the Room table with sample data'

    def handle(self, *args, **kwargs):
        room_types = ['office', 'meeting', 'rehearsal']

        for floor in range(1, 5):  # Floors 1 to 4
            for number in range(1, 16):  # Room numbers 1 to 15
                room_number = f"{floor}0{
                    number}" if number < 10 else f"{floor}{number}"
                # Distribute types evenly
                room_type = room_types[(number - 1) % len(room_types)]

                Room.objects.create(
                    room_number=room_number,
                    capacity=10,  # Example capacity
                    is_available=True,
                    room_type=room_type
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Successfully created room {room_number}'))
