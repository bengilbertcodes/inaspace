from django.contrib import admin
from django.urls import path, include
from bookings.views import custom_login_view, signup

urlpatterns = [
    path('admin/', admin.site.urls),
	path('signup', signup, name='signup'),
	path('login', custom_login_view, name='login'),
]

