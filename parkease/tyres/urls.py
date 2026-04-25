from django.urls import path
from .views import tyre_service,delete_tyre_service


urlpatterns=[
    path('tyre_service',tyre_service,name='tyre_service'),
    path('delete_tyre_service/<int:service_id>',delete_tyre_service,
    name='delete_tyre_service')
    
]