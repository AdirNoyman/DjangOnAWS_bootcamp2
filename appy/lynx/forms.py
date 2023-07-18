# Imports for user registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Imports for user login form
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from . models import Profile

# Create the registration form data model


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

# Create the login form data model


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

# Profile management form for update profile


class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']

# Update our profile picture form


class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file', 'placeholder': 'Profile picture'}))

    class Meta:
        model = Profile
        fields = ['profile_pic']
