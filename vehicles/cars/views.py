from django.shortcuts import render
from .models import Person, Car

# Create your views here.
def greeting(request):
  data={}
  return render(request, "greeting.html", context=data)

def read_cars(request):
  data={}
  all_cars = Car.objects.all()
  data['allc'] = all_cars
  return render(request, "read_cars.html", context=data)

def list_bmw_cars(request):
    data = {}
    all_cars = Car.objects.filter(Model="BMW")
    data['allc'] = all_cars
    return render(request, "read_cars.html", context=data)

def list_2000_cars(request):
   data = {}
   all_cars = Car.objects.filter(year__gte=2000)
   data['allc'] = all_cars
   return render(request, "read_cars.html", context=data)

def list_1990_2000(request):
   data = {}
   all_cars = Car.objects.filter(year_range=["1999", "2000"])
   data['allc'] = all_cars
   return render(request, "read_cars.html", context=data)
   
def list_cars_mohammad_jamal(request):
   data = {}
   person_record = Person.objects.get(name = "mohammad jamal")
   all_cars = person_record.car_set.all()
   data['person'] = person_record
   data['allc'] = all_cars
   return render(request, "read_cars.html", context=data)
   
   
def search_license_id(request):
   data = {}
   return render(request, "read_cars.html", context=data)
