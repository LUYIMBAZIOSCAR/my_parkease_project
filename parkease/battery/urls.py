from django.urls import path
from .views import battery_service

urlpatterns=[
    path('battery_service',battery_service,name='battery_service')
]