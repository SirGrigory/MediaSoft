from django.urls import path, include
from city.views import CitiesList, StreetsList
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city/', CitiesList.as_view(), name='cities'),
    path('city/<int:id>/street', StreetsList.as_view(), name='streets')
]