from django import forms
from .models import TyreService

class TyreServiceForm(forms.ModelForm):
    class Meta:
        model=TyreService
        fields=