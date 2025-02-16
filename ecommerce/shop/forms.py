from django import forms
from django.contrib.auth.models import User

from django.forms import PasswordInput


class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=PasswordInput)

    class Meta:
        model=User
        fields=['username','password','confirm_password','email','first_name','last_name']