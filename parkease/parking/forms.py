from django import forms
from .models import Vehicle
import re

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
            'nin',
            'gender'

        ]

        widgets = {
            'driver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'number_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'nin': forms.TextInput(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages={
            'driver_name':{'required':'Please enter your name'},
            'phone_number':{'required':'Please enter the number plate'},
            'model':{'required':'Please enter the model'},
            'color':{'required':'Please enter the color'},
            'phone_number':{'required':'Please enter your phone number'},
            'nin':{'required':'Please enter your nin','unique':
            'NIN already exists, please enter unique nin'},
            'number_plate':{'required':'Please enter your number plate',
            'unique':'Number already exists, enter unique number plate'},
            'gender':{'required':'Please enter your gender'}

        }

    def clean_driver_name(self):
        name=self.cleaned_data['driver_name']
        if len(name) < 3:
            raise forms.ValidationError('Driver name must be atleast 3 characters')
        if not name.replace(" ","").isalpha():
            raise forms.ValidationError("Driver name must not contain numbers")
        return name
        
    def clean_phone_number(self):
        phone=self.cleaned_data['phone_number']
        if not re.match(r'^07\d{8}$',phone):
            raise forms.ValidationError('Enter a valid phone number e.g 0709135086')
        return phone
        
    def clean_nin(self):
        nin=self.cleaned_data['nin']

        if len(nin) != 14:
            raise forms.ValidationError('NIN must be 14 characters')
            
        return nin
    
    def clean_number_plate(self):
        plate=self.cleaned_data['number_plate'].upper()

        # starting with U
        if not plate.startswith('U'):
            raise forms.ValidationError('Number plate must start U')
        # must be alphanumeric 
        if not plate.isalnum():
            raise forms.ValidationError('Number plate must contain only letters and numbers.')
        
        # must be less than 6 characters 
        if len(plate) >= 6:
            raise forms.ValidationError('Number plate must be less than 6 characters.')
        return plate
            
    
        


    