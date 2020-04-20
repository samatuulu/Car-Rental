from django.db import models
from main import settings


TRANSMISSION_CHOICES = (
        ('M', 'Manual'),
        ('A', 'Automatic'),
)

class CarCategory(models.Model):
    name = models.CharField(max_length=40, verbose_name='Car category')
    
    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=25, verbose_name='Car brand:')
    name = models.CharField(max_length=255, verbose_name='Car name:')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Price:')
    description = models.CharField(max_length=1500, verbose_name='Car description:')
    photo = models.ImageField(upload_to='car_images', verbose_name='Car photo:')
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES, default=TRANSMISSION_CHOICES[0][0], verbose_name='Transmission:')
    car_category = models.ForeignKey('CarCategory', related_name='car', on_delete=models.CASCADE, verbose_name='Car category:')
    author = models.ForeignKey('auth.User', related_name='car',
                               on_delete=models.CASCADE, null=True, blank=True, verbose_name='Author:')

    def __str__(self):
        return self.brand
