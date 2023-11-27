from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import CustomUser, WaitingList
from hacker.models import HackerInfo


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'onblur': 'passwordValidation()'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(
        attrs={'class': 'form-control',  'onblur': 'password2Validation()'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'shirt_size', 'food_preference', 'gender', 'phone',
                  'age', 'school_name', 'level_of_study',
                  'major', 'resume', 'registration_comment'
                  )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jane'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jdoe123@gmail.com', 'type': 'email', 'onblur': 'emailValidation()', "pattern": "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$", "title": "username@domain.tld"}),
            'shirt_size': forms.Select(attrs={'class': 'form-select'}),
            'food_preference': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': "tel", 'placeholder': '7861234567'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control', 'list': 'SchoolOptions'}),
            'major': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'level_of_study': forms.Select(attrs={'class': 'form-select'}),
            'resume': forms.FileInput(attrs={'class': 'form-control form-control-lg', "accept": ".doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,.pdf"}),
            'registration_comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us anything you think we\'d need to know!'})
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
        model = HackerInfo
        fields = ()

        widgets = {
        }


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'shirt_size', 'food_preference', 'gender', 'phone',
                  'age', 'school_name', 'level_of_study',
                  'major', 'registration_comment', 'address')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jane'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Jdoe123@gmail.com', "pattern": "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$", "title": "username@domain.tld"}),
            'shirt_size': forms.Select(attrs={'class': 'form-select'}),
            'food_preference': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': "tel", 'placeholder': '7861234567'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '9000 Pennington Road'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control', 'list': 'SchoolOptions'}),
            'major': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'level_of_study': forms.Select(attrs={'class': 'form-select'}),
            'registration_comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us anything you think we\'d need to know!'})
        }


class WaitingListCreationForm(forms.ModelForm):
    class Meta:
        model = WaitingList
        fields = ('full_name', 'email')

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control transparent'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control transparent'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        if WaitingList.objects.filter(email=email).exists():
            self.add_error('email', "This Email is already on the waitlist!")

        return email
    

