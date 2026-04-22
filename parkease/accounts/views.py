from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from parking.models import Vehicle
from django.db.models import Sum
from django.utils import timezone
from .forms import LoginForm
from tyres.models import TyreService

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)

                role = user.profile.role

                if role == 'admin':
                    return redirect('admin_dashboard')
                elif role == 'attendant':
                    return redirect('attendant_dashboard')
                elif role =='manager1':
                    return redirect('manager1_dashboard')
        
            else:
                messages.error(
                    request,
                    "Invalid username or password. Please try again."
                )

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


# parking attendant dashboard 
def attendant_dashboard(request):
    parked_vehicles=Vehicle.objects.filter(is_parked=True).count()
    total_vehicles=Vehicle.objects.all().count()
    signed_out_vehicles=Vehicle.objects.filter(is_parked=False).count()
    context={
        'parked_vehicles':parked_vehicles,
        'total_vehicles':total_vehicles,
        'signed_out_vehicles':signed_out_vehicles
    }

    return render(request,'accounts/attendant-dashboard.html',context)

# manager dashboard 
def admin_dashboard(request):
    today=timezone.now().date()
    parked_vehicles=Vehicle.objects.filter(is_parked=True).count()
    total_vehicles=Vehicle.objects.all().count()
    signed_out_vehicles=Vehicle.objects.filter(is_parked=False).count()
    total_revenue=Vehicle.objects.filter(is_paid=True).aggregate(total=Sum('fee'))
    daily_revenue=Vehicle.objects.filter(is_paid=True,
    exit_time__date=today).aggregate(total=Sum('fee'))
    
    context={
        'parked_vehicles':parked_vehicles,
        'total_vehicles':total_vehicles,
        'signed_out_vehicles':signed_out_vehicles,
        'total_revenue':total_revenue['total'] or 0,
        'daily_revenue':daily_revenue['total'] or 0
    }

    return render(request,'accounts/admin_dashboard.html',context)
# view function for manager1 dashboard 
def manager1_dashboard(request):
    services=TyreService.objects.all()
    return render(request,'accounts/manager1_dashboard.html',{'services':services})

# view for logout
def logout_view(request):
    logout(request)
    return redirect('login')
