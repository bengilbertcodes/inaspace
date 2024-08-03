from django.views.generic import TemplateView
from django.utils import timezone
from bookings.models import Booking


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            now = timezone.now()
            context['bookings'] = Booking.objects.filter(
                user=self.request.user,
                date__gte=now.date(),
            )
        else:
            context['bookings'] = []
        return context
