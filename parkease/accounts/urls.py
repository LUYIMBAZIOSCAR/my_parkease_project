from django.urls import path
from .views import login_view
from .views import attendant_dashboard
from .views import admin_dashboard
from .views import logout_view
from .views import manager1_dashboard


urlpatterns=[
    path('',login_view,name='login'),
    path('attendant_dashboard',attendant_dashboard,name='attendant_dashboard'),
    path('admin_dashboard',admin_dashboard,name='admin_dashboard'),
    path('logout',logout_view,name='logout'),
    path('manager1_dashboard',manager1_dashboard,name='manager1_dashboard')



]