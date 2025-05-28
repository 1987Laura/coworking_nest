from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("spaces/", views.spaces_view, name="spaces"),
    path("bookings/", views.bookings_view, name="bookings"),
    path("profile/", views.profile_view, name="profile"),
]