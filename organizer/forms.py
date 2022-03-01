from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import fields, widgets

from default.models import CustomUser
from .models import OrganizerInfo, WebsiteSettings, OrganizerPermission, FeaturePermission


class OrganizerCreationForm(forms.Form):

    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "First Name", 'class':'form-control text-center'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Last Name", 'class':'form-control text-center'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Email", 'class':'form-control text-center'}))


    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        if CustomUser.objects.filter(email=email).exists():
            self.add_error('email',"This Email is already in the system!")
        
        return email



class WebsiteSettingsControlForm(forms.ModelForm):
    class Meta:
        model = WebsiteSettings
        fields = ['waiting_list_status']

        widgets = {
            'waiting_list_status': forms.Select(attrs={})
        }

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return member.permission_name[2:].title()

class OrganizerPermissionControlForm(forms.ModelForm):
    class Meta:
        model = OrganizerPermission
        fields = ['permission']

    permission = CustomMMCF(
        queryset=FeaturePermission.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={})
    )




