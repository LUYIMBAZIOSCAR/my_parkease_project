from django.urls import path
from .views import register_vehicle
from .views import parked_vehicles



urlpatterns=[
    path('',register_vehicle,name='register_vehicle'),
    path('parked_vehicles',parked_vehicles,name='parked_vehicles')
    


]