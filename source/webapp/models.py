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
    car_category = models.ForeignKey('webapp.CarCategory', related_name='car', on_delete=models.CASCADE, verbose_name='Car category:')
    author = models.ForeignKey('auth.User', related_name='car',
                               on_delete=models.CASCADE, null=True, blank=True, verbose_name='Author:')

    def __str__(self):
        return self.brand


class Order(models.Model):
    user = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL, 
                                                                verbose_name='User', related_name='oders')
    first_name = models.CharField(max_length=100, verbose_name='Name', null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name='Last name', null=True, blank=True)
    email = models.EmailField(max_length=50, verbose_name='Email', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Phone')
    cars = models.ManyToManyField(Car, verbose_name='Cars', related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last updated')
    
    
    # def __str__(self):
    #     return "{} - {}".format(self.created_at.strftime('%Y-%m-%d %H:%M:%S'),)

    def get_total(self):
        total = 0
        for order_car in self.order_cars:
            total += order_car.get_total()
            return total


class OrderCar(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order', related_name='order_cars')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Car', related_name='order_cars')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')

    def __str__(self):
        return "{} - {}".format(self.car, self.order,)

    def get_total(self):
        return self.amount * self.car.price

    class Meta:
        verbose_name = 'Car booking'
        verbose_name_plural = 'Cars booking'