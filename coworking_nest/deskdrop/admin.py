from django.contrib import admin
from .models import Space, Booking

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location', 'created_at')
    search_fields = ('name', 'location')
    

@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('space', 'user', 'start_date', 'end_date')
    list_filter = ('start_date', 'space')
    