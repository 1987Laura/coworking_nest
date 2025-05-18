from django.shortcuts import render

# Create your views here.

def home_view(request):
	context = {}
	return render(request, 'home.html', context)

def about_view(request):
	context = {}
	return render(request, 'about.html', context)

def spaces_view(request):
	context = {}
	return render(request, 'spaces.html', context)

def bookings_view(request):
	context = {}
	return render(request, 'bookings.html', context)

def profile_view(request):
	context = {}
	return render(request, 'profile.html', context)
