from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username",
        "class": "input"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "input"
    }))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']