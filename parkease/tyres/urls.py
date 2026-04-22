from django.urls import path
from .views import tyre_service

urlpatterns=[
    path('tyre_service',tyre_service,name='tyre_service')
    
]