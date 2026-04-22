from django import forms
from .models import TyreService
import re

class TyreServiceForm(forms.ModelForm):
    class Meta:
        model=TyreService
        fields=[
            'customer_name',
            'phone_number',
            'number_plate',
            'service_type',

        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'number_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages={
            'customer_name':{'required':'Please enter your name'},
            'service_number':{'required':'Please enter the service type'},
            'phone_number':{'required':'Please enter your phone number'},
            'number_plate':{'required':'Please enter your number plate',
            'unique':'Number already exists, enter unique number plate'},
        }
    def clean_customer_name(self):
        name=self.cleaned_data['customer_name']
        if len(name) < 3:
            raise forms.ValidationError('Customer name must be atleast 3 characters')
        if not name.replace(" ","").isalpha():
            raise forms.ValidationError("Customer name must not contain numbers")
        return name
    def clean_phone_number(self):
        phone=self.cleaned_data['phone_number']
        if not re.match(r'^07\d{8}$',phone):
            raise forms.ValidationError('Enter a valid phone number e.g 0709135086')
        return phone
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