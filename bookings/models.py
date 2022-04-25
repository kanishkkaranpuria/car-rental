from django.db import models
from django.contrib.auth import get_user_model
from cars.models import Car
# Create your models here.

User = get_user_model()

class Booking(models.Model):
    name        = models.CharField(max_length=250)
    phoneNumber = models.IntegerField(null=True,blank=True)
    email       = models.EmailField(max_length=255)
    car         = models.ForeignKey("cars.Car", on_delete=models.CASCADE, related_name="car")

    def __str__(self):
        return f'{self.name} - {self.car.name}'