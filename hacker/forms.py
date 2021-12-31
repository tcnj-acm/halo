from default.models import CustomUser
from django import forms
from default.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import hacker


class CustomHackerChangeForm(CustomUserChangeForm):
    class Meta:
        model = hacker
        fields = ('address', 'education','major','shirt_size','food_preference')

        widgets = {
            'address' : forms.TextInput(attrs = {  'placeholder':'Place Holder'}),
            'major' : forms.TextInput(attrs = { 'placeholder':'Place Holder'}),
            'education' : forms.Select(attrs = {}),
            'shirt_size' : forms.Select(attrs = {}),
            'food_preference' : forms.Select(attrs = {}),
        }


    