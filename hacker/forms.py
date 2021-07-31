from default.models import CustomUser
from django import forms
from default.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import hacker

class HackerCreationForm(forms.ModelForm):

    class Meta:
        model = hacker
        fields = ('__all__')
        exclude = ('hacker','checked_in')

    


class CustomHackerChangeForm(CustomUserChangeForm):
    class Meta:
        model = hacker
        fields = ('address', 'education', 'major')
    