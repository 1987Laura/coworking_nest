from django.contrib import admin

# Register your models here.


from .models import Space, Booking
admin.site.register(Space)
admin.site.register(Booking)
