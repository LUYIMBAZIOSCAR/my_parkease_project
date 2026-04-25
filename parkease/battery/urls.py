from django.urls import path
from .views import battery_service,delete_battery_service

urlpatterns=[
    path('battery_service',battery_service,name='battery_service'),
    path('delete_battery_service/<int:service_id>',delete_battery_service,name='delete_battery_service')
]