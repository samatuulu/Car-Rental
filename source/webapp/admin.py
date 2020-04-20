from django.contrib import admin
from .models import Car, CarCategory, Order, OrderCar

admin.site.register(Car)
admin.site.register(CarCategory)
admin.site.register(Order)
admin.site.register(OrderCar)
