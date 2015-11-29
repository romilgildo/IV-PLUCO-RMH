from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
