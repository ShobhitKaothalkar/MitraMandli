from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username' , 'email' , 'password1' , 'password2']


class UserProfileForm(ModelForm):

    class Meta:
        model  = UserProfile
        exclude = ['user']