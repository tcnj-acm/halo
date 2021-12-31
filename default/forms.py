from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import CustomUser
from hacker.models import hacker

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': "Password"}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': "Password Confirmation"}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name' : forms.TextInput(attrs = {'placeholder':'First Name'}),
            'last_name' : forms.TextInput(attrs = {'placeholder':'Last Name'}),
            'email' : forms.TextInput(attrs = {'placeholder':'Email Address'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class HackerCreationForm(forms.ModelForm):

    class Meta:
        model = hacker
        fields = ('address', 'education','major','shirt_size','food_preference')

        widgets = {
            'address' : forms.TextInput(attrs = {'placeholder':''}),
            'major' : forms.TextInput(attrs = {'placeholder':'Other'}),
            'education' : forms.Select(attrs = {}),
            'shirt_size' : forms.Select(attrs = {}),
            'food_preference' : forms.Select(attrs = {}),
        }

class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password', 'is_active', 'is_admin', 'is_superuser')