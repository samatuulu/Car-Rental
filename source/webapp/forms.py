from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'name', 'price', 'description', 'photo', 'transmission', 'car_category')