
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def spaces_view(request):
    return render(request, 'spaces.html')

def bookings_view(request):
    return render(request, 'bookings.html')

def profile_view(request):
    return render(request, 'profile.html')