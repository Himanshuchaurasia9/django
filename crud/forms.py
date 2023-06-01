from django import forms 
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','phone','email','password']
        widgets = {
            'name': forms.TextInput(attrs={
                'class' :'form-control'
            }),'phone': forms.NumberInput(attrs={
                'class' :'form-control'
            }),'email': forms.EmailInput(attrs={
                'class' :'form-control'
            }),'password': forms.PasswordInput(render_value =True, attrs={
                'class' :'form-control'
            }),
        }