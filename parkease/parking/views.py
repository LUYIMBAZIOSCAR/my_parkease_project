from django.shortcuts import render,redirect
from .forms import VehicleForm
from django.contrib import messages
from .models import Vehicle

# Create your views here.

# view for registering a vehicle 

def register_vehicle(request):
    if request.method=='POST':
        form=VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Vehicle registered successfully')
            return redirect('attendant_dashboard')
    else:
        form=VehicleForm()
        
    return render(request,'parking/register_vehicle.html',{"form":VehicleForm()})

# View function for parked vehicles 
def parked_vehicles(request):
    vehicles=Vehicle.objects.filter(is_parked=True)

    for vehicle in vehicles:
        vehicle.fee=vehicle.calculate_fee()

    return render(request,'parking/parked_vehicles.html',{'vehicles':vehicles})

