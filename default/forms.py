from multiprocessing import Event
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import CustomUser, WaitingList, Event
from hacker.models import HackerInfo
import datetime

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'onblur':'passwordValidation()'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control',  'onblur':'password2Validation()'}))

    class Meta:
        model = CustomUser
        fields = (  'first_name', 'last_name', 'email',
                    'shirt_size','food_preference', 'gender', 
                    'age', 'school_name','level_of_study',
                    'major', 'resume','registration_comment' 
        )

        widgets = {
            'first_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'email' : forms.TextInput(attrs = {'class':'form-control', 'type':'email', 'onblur':'emailValidation()', "pattern":"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$", "title":"username@domain.tld" }),
            'shirt_size' : forms.Select(attrs = {'class':'form-select'}),
            'food_preference' : forms.Select(attrs = {'class':'form-select'}),
            'gender' : forms.Select(attrs = {'class':'form-select'}),
            'school_name' : forms.TextInput(attrs = {'class':'form-control', 'list':'SchoolOptions'}),
            'major' : forms.Select(attrs = {'class':'form-select'}),
            'age' : forms.NumberInput(attrs = {'class':'form-control'}),
            'level_of_study' : forms.Select(attrs = {'class':'form-select'}),
            'resume' : forms.FileInput(attrs = {'class':'form-control form-control-lg',"accept":".doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,.pdf"}),
            'registration_comment' : forms.Textarea(attrs = {'class':'form-control'})
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
                    'shirt_size','food_preference', 'gender', 
                    'age', 'school_name','level_of_study',
                    'major','registration_comment', 'address')

        widgets = {
            'first_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'email' : forms.TextInput(attrs = {'class':'form-control', 'type':'email', "pattern":"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$", "title":"username@domain.tld" }),
            'shirt_size' : forms.Select(attrs = {'class':'form-select'}),
            'food_preference' : forms.Select(attrs = {'class':'form-select'}),
            'gender' : forms.Select(attrs = {'class':'form-select'}),
            'address' : forms.TextInput(attrs = {'class':'form-control'}),
            'school_name' : forms.TextInput(attrs = {'class':'form-control', 'list':'SchoolOptions'}),
            'major' : forms.Select(attrs = {'class':'form-select'}),
            'age' : forms.NumberInput(attrs = {'class':'form-control'}),
            'level_of_study' : forms.Select(attrs = {'class':'form-select'}),
            'registration_comment' : forms.Textarea(attrs = {'class':'form-control'})
        }


class WaitingListCreationForm(forms.ModelForm):
    class Meta:
        model = WaitingList
        fields = ('full_name', 'email')

        widgets = {
            'full_name' : forms.TextInput(attrs = { 'placeholder':'Full Name', 'class':'form-control transparent'}),
            'email' : forms.TextInput(attrs = { 'placeholder':'Email', 'class':'form-control transparent'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        if WaitingList.objects.filter(email=email).exists():
            self.add_error('email',"This Email is already on the waitlist!")
        
        return email

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ( "title", "description", "start_time", "end_time", "date")

    def clean_date(self):
        date = self.cleaned_data['date']
        start = self.cleaned_data['start_time']
        end = self.cleaned_data['end_time']

        HackTCNJ_saturday = datetime.date(2021, 4, 9)
        HackTCNJ_sunday = datetime.date(2021, 4, 10)

        HackTCNJ_start_time = datetime.time(10,0,0)
        HackTCNJ_end_time = datetime.time(16,0,0)
            

        if date == HackTCNJ_saturday:
            if start <  HackTCNJ_start_time:
                self.add_error('start_time', "Start time must be after event hackathon has started")
        elif date == HackTCNJ_sunday:
            if end > HackTCNJ_end_time:
                self.add_error('end_time', "End time must be before ending of hackathon")
        else:
            self.add_error('date', "Date must be on Saturday or Sunday")

        return date
    
        
