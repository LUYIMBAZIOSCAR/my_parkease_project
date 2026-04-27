import uuid
from django.shortcuts import render,redirect,get_object_or_404
from .forms import VehicleForm
from django.contrib import messages
from .models import Vehicle
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required


# Create your views here.

# view for registering a vehicle 
@login_required
def register_vehicle(request):
    if request.user.profile.role != 'attendant':
        return redirect('login')
    if request.method=='POST':
        form=VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Vehicle registered successfully')
            return redirect('attendant_dashboard')
    else:
        form=VehicleForm()
        
    return render(request,'parking/register_vehicle.html',{"form":form})

# View function for parked vehicles 
@login_required
def parked_vehicles(request):
    vehicles=Vehicle.objects.filter(is_parked=True).order_by('-entry_time')

    for vehicle in vehicles:
        vehicle.fee=vehicle.calculate_fee()
    return render(request,'parking/parked_vehicles.html',{'vehicles':vehicles})

# view function for payment confirmation 
@login_required
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
@login_required
def receipt(request,vehicle_id):
    vehicle=get_object_or_404(Vehicle,id=vehicle_id)
    context={'vehicle':vehicle}

    return render(request,'parking/receipt.html',context)

#view function for downloading receipt pdf
@login_required
def download_receipt(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    # creating the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{vehicle.id}.pdf"'

    # creating the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Header
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "PARKING RECEIPT")
    
    # Body
    p.setFont("Helvetica", 12)
    lines = [
        f"Driver: {vehicle.driver_name}",
        f"Receipt No: {vehicle.receipt_number}",
        f"Plate: {vehicle.number_plate}",
        f"Contact: {vehicle.phone_number}",
        f"Gender:{vehicle.gender}",
        f"NIN: {vehicle.nin}",
        f"Entry: {vehicle.entry_time.strftime('%Y-%m-%d %H:%M')}",
        f"Exit: {vehicle.exit_time.strftime('%Y-%m-%d %H:%M') if vehicle.exit_time else 'N/A'}",
        "-----------------------------------------",
        f"TOTAL AMOUNT: Shs {vehicle.fee if vehicle.fee is not None else 0:,}"
    ]

    y = 770
    for line in lines:
        p.drawString(100, y, line)
        y -= 20 # Move down 20 units for each line

    # closing down the pdf cleanly
    p.showPage()
    p.save()

    return response

# view function for signed out vehicles
@login_required
def signed_out_vehicles(request):
    vehicles=Vehicle.objects.filter(is_parked=False).order_by('-exit_time')
    for vehicle in vehicles:
        vehicle.fee=vehicle.calculate_fee()
    
    return render(request,'parking/signed_out_vehicles.html',{'vehicles':vehicles})

# view function to delete a vehicle
@login_required
def delete_vehicle(request,vehicle_id):
    try:
        vehicle=get_object_or_404(Vehicle,id=vehicle_id)

        if request.method=='POST':
            vehicle.delete()
            messages.success(request,'Vehicle deleted successfully')

    except Vehicle.DoesNotExist:
        messages.error(request,'Vehicle already deleted')

    return redirect('records')


