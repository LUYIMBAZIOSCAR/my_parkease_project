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
            'driver_name':{'required':'Please enter your name'},
            'phone_number':{'required':'Please enter the number plate'},
            'model':{'required':'Please enter the model'},
            'color':{'required':'Please enter the color'},
            'phone_number':{'required':'Please enter your phone number'},
            'nin':{'required':'Please enter your nin'},
            'number_plate':{'required':'Please enter your number plate'}

        }

    