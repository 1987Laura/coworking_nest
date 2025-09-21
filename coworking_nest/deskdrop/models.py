from django.db import models
from django.contrib.auth.models import User


class Space(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)  # Preț în RON
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='spaces/', null=True, blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    date = models.DateField()  # ziua rezervării
    start_time = models.TimeField()  # ora de început
    hours_reserved = models.PositiveIntegerField()  # număr de ore rezervate

    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # calculat automat
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.space} pe {self.date} la {self.start_time}"
    
    def save(self, *args, **kwargs):
        price_per_hour = self.space.price_per_day / 8  # calculăm pe baza prețului pe zi
        self.total_price = price_per_hour * self.hours_reserved
        super().save(*args, **kwargs)



