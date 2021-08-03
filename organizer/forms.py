from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import organizer


class NewOrganizer(forms.Form):

    fname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "First Name"}))
    lname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Last Name"}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Email"}))
