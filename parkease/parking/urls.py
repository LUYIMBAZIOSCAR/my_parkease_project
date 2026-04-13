from django.urls import path
from .views import register_vehicle
from .views import parked_vehicles
from .views import confirm_payment
from .views import receipt
from .views import download_receipt
from .views import signed_out_vehicles
from .views import delete_vehicle


urlpatterns=[
    path('',register_vehicle,name='register_vehicle'),
    path('parked_vehicles',parked_vehicles,name='parked_vehicles'),
    path('confirm_payment/<int:vehicle_id>',confirm_payment,
         name='confirm_payment'),
    path('receipt/<int:vehicle_id>',receipt,name='receipt'),
    path('download_receipt/<int:vehicle_id>',download_receipt,name='download_receipt'),
    path('signed_out_vehicles',signed_out_vehicles,name='signed_out_vehicles'),
    path('delete_vehicle/<int:vehicle_id>',delete_vehicle,name='delete_vehicle')


]