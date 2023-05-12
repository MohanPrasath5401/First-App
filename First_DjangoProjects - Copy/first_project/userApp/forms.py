from socket import fromshare
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class SignUP(UserCreationForm):
    #email = forms.EmailField() #this email field existing from User model 
    email = forms.EmailField(label = "EmailNow")

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):#for auth user
    class Meta:
        model = User
        fields = ['email']   #this email field already present in auth table

class ProfileUpdateForm(forms.ModelForm):#for Profile user
    class Meta:
        model = Profile
        fields = ['age','image']







