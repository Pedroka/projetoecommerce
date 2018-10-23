#coding = utf-8

from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','name']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','name']