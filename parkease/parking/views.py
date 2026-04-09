from django.shortcuts import render,redirect
from django import forms
from .models import Vehicle
from django.contrib import messages

# Create your views here.

# view for registering a vehicle 
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'driver_name',
            'vehicle_type',
            'number_plate',
            'model',
            'color',
            'phone_number',
            'nin'
        ]

        widgets = {
            'driver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'number_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'nin': forms.TextInput(attrs={'class': 'form-control'}),
        }

    #   validation
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')

        if not phone.isdigit():
            raise forms.ValidationError("Phone must contain only digits")

        if not phone.startswith('07') or len(phone) != 10:
            raise forms.ValidationError("Enter a valid Ugandan number (07XXXXXXXX)")

        return phone



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
    return render(request,'parking/parked_vehicles.html',{'vehicles':vehicles})

