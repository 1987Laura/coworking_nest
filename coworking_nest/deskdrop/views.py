
from django.shortcuts import render
from .models import Space

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def spaces_view(request):
    spaces = Space.objects.all()  # Preia toate spațiile din baza de date
    return render(request, 'spaces.html', {'spaces': spaces})
    

def bookings_view(request):
    return render(request, 'bookings.html')

def profile_view(request):
    return render(request, 'profile.html')