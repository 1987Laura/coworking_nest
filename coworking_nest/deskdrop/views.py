
from django.shortcuts import render, get_object_or_404, redirect
from .models import Space, Booking

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

def space_list(request):
    spaces = Space.objects.all()
    return render(request, 'spaces.html', {'spaces': spaces})

def book_space(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    return render(request, 'book_space.html', {'space': space})

def bookings(request):
    if not request.user.is_authenticated:
        # utilizatorul nu e logat -> afișăm mesajul cu butoane
        return render(request, 'not_authenticated.html') 

    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': user_bookings})

def terms_view(request):
    return render(request, 'terms.html')

def privacy_view(request):
    return render(request, 'privacy.html')