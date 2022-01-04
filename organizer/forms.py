from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import fields, widgets
from .models import OrganizerInfo, WebsiteSettings, WaitingListSupervisor


class OrganizerCreationForm(forms.Form):

    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "First Name"}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Last Name"}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Email"}))


class WaitingListControlForm(forms.ModelForm):
    class Meta:
        model = WebsiteSettings
        fields = ['waiting_list_status']

        widgets = {
            'waiting_list_status' : forms.Select(attrs = {})
        }


class WaitingListSuperVisorForm(forms.ModelForm):
    class Meta:
        model = WaitingListSupervisor
        fields = ['email',]

        widgets = {
            'email' : forms.TextInput(attrs = {'placeholder':'Email Address'}),
        }