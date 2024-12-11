from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'}))

    class Meta:
        
        model = User
        fields = ['email' ,'username' , 'password1', 'password2']
