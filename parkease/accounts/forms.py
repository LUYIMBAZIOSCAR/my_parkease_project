from django import forms

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

