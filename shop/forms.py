from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import model_to_dict
from  .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class Order(forms.ModelForm):
#     class meta:
#         model=Product


class RegisterUser(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={
            'username': forms.TextInput(attrs={ 'class':"form-control" ,'id':"username",'placeholder':"Your username..."}),
            'email':forms.EmailInput(attrs={ 'class':"form-control" ,'id':"email",'placeholder':"Your email address..."}),
            'password':forms.PasswordInput(attrs={ 'class':'form-control' ,'id':"password",'placeholder':"Your passowrd..."})

        }

