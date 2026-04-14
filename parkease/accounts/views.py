from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from parking.models import Vehicle

# Create your views here.

def login_view(request):
    if request.method=="POST":
        body=request.POST
        username=body.get('username')
        password=body.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            role=user.profile.role
            if role=='admin':
                return redirect('admin_dashboard')
            elif role=='attendant':
                return redirect('attendant_dashboard')

            
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request,'accounts/login.html')


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
    parked_vehicles=Vehicle.objects.filter(is_parked=True).count()
    total_vehicles=Vehicle.objects.all().count()
    signed_out_vehicles=Vehicle.objects.filter(is_parked=False).count()
    context={
        'parked_vehicles':parked_vehicles,
        'total_vehicles':total_vehicles,
        'signed_out_vehicles':signed_out_vehicles
    }

    return render(request,'accounts/admin_dashboard.html',context)

# view for logout
def logout_view(request):
    logout(request)
    return redirect('login')
