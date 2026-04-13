import uuid
from django.shortcuts import render,redirect,get_object_or_404
from .forms import VehicleForm
from django.contrib import messages
from .models import Vehicle
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas

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
    vehicle=get_object_or_404(Vehicle,id=vehicle_id)
    fee=vehicle.calculate_fee()
    context={
            'vehicle':vehicle,
            'fee':fee
        }

    if request.method=='POST':
        vehicle.exit_time=timezone.now()
        vehicle.fee=fee
        vehicle.is_paid=True
        vehicle.is_parked=False
        vehicle.receipt_number=str(uuid.uuid4())[:8]

        vehicle.save()
       

        return redirect('receipt',vehicle_id=vehicle_id)
    
    return render(request,'parking/confirm_payment.html',context)

# view function for the receipt
def receipt(request,vehicle_id):
    vehicle=get_object_or_404(Vehicle,id=vehicle_id)
    context={'vehicle':vehicle}

    return render(request,'parking/receipt.html',context)

#view function for downloading receipt pdf
def download_receipt(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{vehicle.id}.pdf"'

    p = canvas.Canvas(response)

    p.drawString(100, 800, "Parking Receipt")
    p.drawString(100, 780, f"Receipt No: {vehicle.receipt_number}")
    p.drawString(100, 760, f"Driver: {vehicle.driver_name}")
    p.drawString(100, 740, f"Plate: {vehicle.number_plate}")
    p.drawString(100, 720, f"Entry: {vehicle.entry_time}")
    p.drawString(100, 700, f"Exit: {vehicle.exit_time}")
    p.drawString(100, 680, f"Amount: Shs {vehicle.fee}")

    p.showPage()
    p.save()

    return response

# view function for signed out vehicles
def signed_out_vehicles(request):
    vehicles=Vehicle.objects.filter(is_parked=False)

    for vehicle in vehicles:
        vehicle.fee=vehicle.calculate_fee()
    
    return render(request,'parking/signed_out_vehicles.html',{'vehicles':vehicles})

# view function to delete a vehicle
def delete_vehicle(request,vehicle_id):
    try:
        vehicle=get_object_or_404(Vehicle,id=vehicle_id)

        if request.method=='POST':
            vehicle.delete()
            messages.success(request,'Vehicle deleted successfully')

    except Vehicle.DoesNotExist:
        messages.error(request,'Vehicle already deleted')

    return redirect('signed_out_vehicles')


