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
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Calculat automat
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.space.name} ({self.start_date})"
