from django.contrib import admin
from .models import Space, Booking

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location', 'created_at', 'image_preview')
    search_fields = ('name', 'location')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'
    

@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'space', 'date', 'start_time', 'hours_reserved', 'total_price')
    list_filter = ('date',)

    