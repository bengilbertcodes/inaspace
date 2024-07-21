from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Booking
from .forms import CustomLoginForm, SignUpForm, BookingRequestForm


def custom_login_view(request):
    form = CustomLoginForm(request=request, data=request.POST or None)
    if form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        login(request, user)
        messages.success(request, 'Successfully logged in')
        return redirect('home')
    return render(request, 'account/custom_login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(
                request, username=username, password=password)
            login(request, user)  # Automatically log in the user after sign-up
            messages.success(request, 'Account created successfully.')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def booking_request(request):
    form_class = BookingRequestForm
    template_name = 'booking/booking_request.html'
    model = Booking
    
	
