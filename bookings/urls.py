from django.contrib import admin
from django.urls import path, include
from bookings.views import custom_login_view, app_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('signup/', app_views.signup, name='signup'),
	path('login/', custom_login_view, name='login'),
]

