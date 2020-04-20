from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from .models import Car

from django.urls import reverse
from .forms import CarForm

class CarListView(ListView):
    model = Car
    template_name = 'templates/car_list.html'
    context_object_name = 'cars'


class CarCreateView(PermissionRequiredMixin, CreateView):
    model = Car
    template_name = 'webapp/car_create.html'
    form_class = CarForm
    permission_required = 'add_car'
    permission_denied_messsage = 'Access denied!'

    def form_valid(self, form):
        if str(self.request.user) != 'AnonymousUser':
            form.instance.author = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('cars')

class CarDetailView(DetailView):
    model = Car
    template_name = 'webapp/car_detail.html'
    context_object_name = 'car'

class CarUpdateView(UserPassesTestMixin, UpdateView):
    model = Car
    template_name = 'webapp/car_update.html'
    fields = ('brand', 'name', 'price', 'description', 'photo', 'transmission', 'car_category')
    contex_object_name = 'car'


    def test_func(self):
        if self.request.user.has_perm('change_car') or self.get_object().author == self.request.user:
            return True

    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.pk})


def car_delete(request, pk):
    query = Car.objects.get(pk=pk)
    query.delete()
    return redirect('cars')
