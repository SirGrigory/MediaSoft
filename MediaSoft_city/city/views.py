from django.shortcuts import render
from django.views.generic import ListView
from city.models import City, Street, Shop
from django.http import request
# Create your views here.

class CitiesList(ListView):
    model = City
    context_object_name = 'cities'
    template_name = 'city/cities.html'


def home(request):
    return render(request, 'city/home.html')
    

