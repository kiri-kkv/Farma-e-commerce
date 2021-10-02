from django import forms
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    Enter_your_image=forms.ImageField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields=["Enter_your_image","username", "email", "password1", "password2"]
