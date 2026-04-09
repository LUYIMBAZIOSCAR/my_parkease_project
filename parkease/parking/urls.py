from django.urls import path
from .views import register_vehicle



urlpatterns=[
    path('',register_vehicle,name='register_vehicle')

]