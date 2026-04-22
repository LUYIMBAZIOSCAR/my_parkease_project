from django import forms
from .models import BatteryService
import re

class BatteyServiceForm(forms.ModelForm):
    class Meta:
        model=BatteryService
        fields=[
            'customer_name',
            'phone_number',
            'battery_type',
            'service_type'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'battery_type': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages={
            'customer_name':{'required':'Please enter your name'},
            'service_type':{'required':'Please select service type'},
            'phone_number':{'required':'Please enter your phone number'},
            'battery_type':{'required':'Please select battery type'},
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
    