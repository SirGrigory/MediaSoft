from django.urls import path, include
from city.views import CitiesList
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city/',CitiesList.as_view(), name='cities')
]