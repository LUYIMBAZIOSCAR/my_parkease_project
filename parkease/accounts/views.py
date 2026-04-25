from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from parking.models import Vehicle
from django.db.models import Sum
from django.utils import timezone
from .forms import LoginForm
from tyres.models import TyreService
from battery.models import BatteryService
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import CreateUserForm


# Create your views here.

# view function for creating a user

@login_required
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone_number']
            role = form.cleaned_data['role']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            else:
                user = User.objects.create_user(username=username,password=password)
                Profile.objects.create(user=user,phone_number=phone,role=role)
                messages.success(request, "User created successfully.")
                return redirect('create_user')
    else:
        form=CreateUserForm()

    return render(request,'accounts/register_user.html',{'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request, user)
                role = user.profile.role
                if role == 'admin':
                    return redirect('admin_dashboard')
                elif role == 'attendant':
                    return redirect('attendant_dashboard')
                elif role =='manager1':
                    return redirect('manager1_dashboard')
                elif role == 'manager2':
                    return redirect('manager2_dashboard')
        
            else:
                messages.error(request,"Invalid username or password. Please try again.")
    else:
        form=LoginForm()

    return render(request,'accounts/login.html',{'form': form})


# parking attendant dashboard
@login_required 
def attendant_dashboard(request):
    # Only attendant allowed
    if request.user.profile.role != 'attendant':
        return redirect('login')
    parked_vehicles=Vehicle.objects.filter(is_parked=True).count()
    total_vehicles=Vehicle.objects.all().count()
    signed_out_vehicles=Vehicle.objects.filter(is_parked=False).count()
    context={
        'parked_vehicles':parked_vehicles,
        'total_vehicles':total_vehicles,
        'signed_out_vehicles':signed_out_vehicles
    }

    return render(request,'accounts/attendant-dashboard.html',context)

# admin dashboard 
@login_required
def admin_dashboard(request):
    # Only admin allowed
    if request.user.profile.role != 'admin':
        return redirect('login')
    today=timezone.now().date()
    vehicles=Vehicle.objects.filter(is_parked=False).order_by('-exit_time')[:3]
    parked_vehicles=Vehicle.objects.filter(is_parked=True).count()
    total_vehicles=Vehicle.objects.all().count()
    signed_out_vehicles=Vehicle.objects.filter(is_parked=False).count()
    parking_revenue=Vehicle.objects.filter(is_paid=True).aggregate(total=Sum('fee'))
    tyre_revenue=TyreService.objects.aggregate(total=Sum('amount'))
    battery_revenue=BatteryService.objects.aggregate(total=Sum('amount'))
    context={
        'vehicles':vehicles,
        'parked_vehicles':parked_vehicles,
        'total_vehicles':total_vehicles,
        'signed_out_vehicles':signed_out_vehicles,
        'parking_revenue':parking_revenue['total'] or 0,
        'tyre_revenue':tyre_revenue['total'] or 0,
        'battery_revenue':battery_revenue['total'] or 0
        

    }

    return render(request,'accounts/admin_dashboard.html',context)

# view function for users 
@login_required
def users(request):
    users=Profile.objects.all()
    return render(request,'accounts/users.html',{'users':users})

# view function to delete a user
@login_required
def delete_user(request,user_id):
    if request.user.profile.role != 'admin':
        return redirect('login')
    profile=get_object_or_404(Profile,id=user_id)
    if request.method=='POST':
            profile.delete()
            messages.success(request,'User deleted successfully')
            return redirect('users')
    return redirect('users')
@login_required
def records(request):
    vehicles=Vehicle.objects.filter(is_parked=False)
    tyre_services=TyreService.objects.all()
    battery_services=BatteryService.objects.all()
    for vehicle in vehicles:
        vehicle.fee=vehicle.calculate_fee()

        
    context={
        'vehicles':vehicles,
        'tyre_services':tyre_services,
        'battery_services':battery_services
    }

    return render(request,'accounts/records.html',context)

# view function for manager1 dashboard 
@login_required
def manager1_dashboard(request):
    # Only tyre manager allowed
    if request.user.profile.role != 'manager1':
        return redirect('login')

    services=TyreService.objects.all()
    return render(request,'accounts/manager1_dashboard.html',{'services':services})

# view function for manager2 dashboard 
@login_required
def manager2_dashboard(request):
    # Only battery manager allowed
    if request.user.profile.role != 'manager2':
        return redirect('login')
    services=BatteryService.objects.all()
    return render(request,'accounts/manager2_dashboard.html',{'services':services})

# view for logout
def logout_view(request):
    logout(request)
    return redirect('login')
