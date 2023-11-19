from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting, name= 'greeting'),
    path('readc/', views.read_cars, name= 'allcars'),
    path('readbmw/', views.read_cars, name='bmws'),
    path('readyear/', views.read_cars, name= 'year__gte=2000'),
    path('readn/', views.read_cars, name= '1990, 2000'),
    path('KWT123/', views.read_cars, name= 'license_id'),
   
]