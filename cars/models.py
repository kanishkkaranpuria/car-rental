from django.db import models

# Create your models here.
class Car(models.Model):
    name      = models.CharField(max_length=50, unique=True)
    price     = models.IntegerField(null=True, default=None)

    def __str__(self):
        return self.name

class Image(models.Model):
    car       = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="carname")
    image     = models.ImageField( upload_to='', max_length=None)

    def __str__(self):
        return self.car.name