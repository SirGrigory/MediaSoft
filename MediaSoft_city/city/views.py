from django.shortcuts import render
from django.views.generic import ListView, DetailView
from city.models import City, Shop, Street
from django.http import request


class CitiesList(ListView):
    model = City
    context_object_name = 'cities'
    template_name = 'city/cities.html'


class StreetsList(ListView):
    model = Street
    context_object_name = 'streets'
    template_name = 'city/streets.html'

    def get_queryset(self):
        return City.objects.all().filter(pk=self.kwargs.get('pk'))


def home(request):
    return render(request, 'city/home.html')
    

