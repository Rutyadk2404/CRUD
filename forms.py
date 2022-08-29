from dataclasses import field
from msilib.schema import Control
from tkinter import Widget
from django.core import validators
from django import forms
from.models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model= User
        fields=['name','email','password']
        Widgets={
            'name':forms.TextInput(attrs={'class':'form-Control'}),
            'email':forms.EmailInput(attrs={'class':'form-Control'}),
            'password':forms.PasswordInput(attrs={'class':'form-Control'}),
        }