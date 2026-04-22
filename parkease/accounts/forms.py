from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        error_messages={
            'required': 'Username is required.'
        }
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        error_messages={
            'required': 'Password is required.'
        }
    )


class CreateUserForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

