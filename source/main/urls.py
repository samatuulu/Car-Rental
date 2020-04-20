"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import CarListView, CarCreateView, CarDetailView, CarUpdateView, car_delete



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', CarListView.as_view(), name='cars'),
    path('car/create/', CarCreateView.as_view(), name='car_create'),
    path('car/detail/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/update/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
    path('car/delete/<int:pk>/', car_delete, name='car_delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
