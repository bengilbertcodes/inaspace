from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bookings.models import Booking


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Allow unauthenticated users to access the home page
            return super().dispatch(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['bookings'] = Booking.objects.filter(
                user=self.request.user)
        else:
            # Different view for unauthenticated users
            context['bookings'] = []
        return context
