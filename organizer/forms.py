from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import fields, widgets
from .models import OrganizerInfo, WebsiteSettings, OrganizerPermission, FeaturePermission


class OrganizerCreationForm(forms.Form):

    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "First Name"}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Last Name"}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Email"}))


class WebsiteSettingsControlForm(forms.ModelForm):
    class Meta:
        model = WebsiteSettings
        fields = ['waiting_list_status']

        widgets = {
            'waiting_list_status': forms.Select(attrs={})
        }

class OrganizerPermissionControlForm(forms.ModelForm):
    class Meta:
        model = OrganizerPermission
        fields = ['user', 'permission']

    permission = forms.ModelMultipleChoiceField(
        queryset=FeaturePermission.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )



