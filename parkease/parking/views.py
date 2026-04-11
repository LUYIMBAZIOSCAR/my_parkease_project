import uuid
from django.shortcuts import render,redirect,get_object_or_404
from .forms import VehicleForm
from django.contrib import messages
from .models import Vehicle
from django.utils import timezone

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

# view function for payment confirmation 
def confirm_payment(request,vehicle_id):
    vehicle=get_object_or_404(Vehicle,vehicle_id)
    fee=vehicle.calculate_fee()

    if request.method=='POST':
        vehicle.exit_time=timezone.now()
        vehicle.fee=fee
        vehicle.is_paid=True
        vehicle.is_parked=False
        vehicle.receipt_number=str(uuid.uuid4())[:8]

        vehicle.save()
        context={
            'vehicle':vehicle,
            'fee':fee
        }

        return redirect('receipt',vehicle_id=vehicle_id)
    
    return render(request,'parking/confirm_payment.html',context)

# view function for the receipt
def receipt(request,vehicle_id):
    vehicle=get_object_or_404(Vehicle,vehicle_id)
    context={'vehicle':vehicle}

    return render(request,'parking/receipt.html',context)


