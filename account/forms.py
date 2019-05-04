from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

        #class Add kore aivabe
        widgets ={
            'email' : forms.EmailInput(attrs={'class': 'myemail'})
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')