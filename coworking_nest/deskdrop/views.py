
from django.shortcuts import render, get_object_or_404, redirect
from .models import Space, Booking
from django.contrib.auth.decorators import login_required
from datetime import datetime

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

@login_required
def book_space(request, space_id):
    space = get_object_or_404(Space, id=space_id)

    if request.method == "POST":
        date = request.POST.get("date")
        start_time = request.POST.get("start_time")
        hours_reserved = request.POST.get("hours_reserved")

        if not date or not start_time or not hours_reserved:
            return render(request, "book_space.html", {
                "space": space,
                "error": "Completează toate câmpurile."
            })

        hours_reserved = int(hours_reserved)

        # calculăm price_per_hour pe baza lui price_per_day
        price_per_hour = space.price_per_day / 8
        total_price = price_per_hour * hours_reserved

        Booking.objects.create(
            user=request.user,
            space=space,
            date=date,
            start_time=start_time,
            hours_reserved=hours_reserved,
            total_price=total_price
        )

        return redirect("bookings")  # sau pagina de succes

    return render(request, "book_space.html", {"space": space})


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