from django.urls import path
from .views import login_view
from .views import attendant_dashboard
from .views import admin_dashboard
from .views import logout_view
from .views import manager1_dashboard
from .views import manager2_dashboard
from .views import create_user
from .views import users
from .views import delete_user
from .views import records


urlpatterns=[
    path('',login_view,name='login'),
    path('attendant_dashboard',attendant_dashboard,name='attendant_dashboard'),
    path('admin_dashboard',admin_dashboard,name='admin_dashboard'),
    path('logout',logout_view,name='logout'),
    path('manager1_dashboard',manager1_dashboard,name='manager1_dashboard'),
    path('manager2_dashboard',manager2_dashboard,name='manager2_dashboard'),
    path('create_user',create_user,name='create_user'),
    path('users',users,name='users'),
    path('delete_user/<int:user_id>',delete_user,name='delete_user'),
    path('records',records,name='records')




]