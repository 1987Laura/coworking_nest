from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("about/", views.about_view, name="about"),
    path("spaces/", views.space_list, name='spaces'),
    path('spaces/<int:space_id>/book/', views.book_space, name='book_space'),
    path("bookings/", views.bookings, name="bookings"),
    path("book/<int:space_id>/", views.book_space, name="book_space"),
    #path("profile/", views.profile_view, name="profile"),
    path('terms/', views.terms_view, name='terms'),
    path('privacy/', views.privacy_view, name='privacy'),
   
]

