from django import forms
from .models import Vehicle

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
        error_messages={
            'driver_name':{'required':'Driver name required'},
            'phone_number':{'required':'Phone is required '}

        }

    