from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import fields, widgets
from .models import WaitingListSupervisors, organizer, WaitingListControl


class NewOrganizer(forms.Form):

    fname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "First Name"}))
    lname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Last Name"}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Email"}))


class WaitingListControlForm(forms.ModelForm):
    class Meta:
        model = WaitingListControl
        fields = ['waiting_list_status']

        widgets = {
            'waiting_list_status' : forms.Select(attrs = {})
        }


class AddWaitingListSupervisor(forms.ModelForm):
    class Meta:
        model = WaitingListSupervisors
        fields = ['email',]

        widgets = {
            'email' : forms.TextInput(attrs = {'placeholder':'Email Address'}),
        }