from django.urls import path
from .views import profile_view
from .views import bookings_view
from .views import spaces_view
from .views import about_view
from .views import home_view

urlpatterns = [

	path("home", home_view),
	path("about", about_view),
	path("spaces", spaces_view),
	path("bookings", bookings_view),
	path("profile", profile_view),
]
