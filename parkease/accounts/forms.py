from django import forms
from .models import Profile

class LoginForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            ''
        ]

