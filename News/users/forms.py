from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.base import Model

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

# username, email, password : default


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
