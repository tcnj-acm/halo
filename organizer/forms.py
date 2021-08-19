from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import organizer
from default.models import event
import datetime as dt

class NewOrganizer(forms.Form):

    fname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "First Name"}))
    lname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Last Name"}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Email"}))

class NewEvent(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewEvent, self).__init__(*args, **kwargs) 



        AVAIL_HOURS = []
        for x in range(0, 24 - 3):
            internal_time = (dt.time(hour=((x//2)), minute=((x % 2) * 30)))
            display_time = internal_time.strftime("%I:%M %p")
            temp_tuple = (internal_time, display_time)
            AVAIL_HOURS.append(temp_tuple)
        self.fields['start_time'] = forms.ChoiceField(choices=AVAIL_HOURS)
        self.fields['end_time'] = forms.ChoiceField(choices=AVAIL_HOURS)

    class Meta:
        model = event
        fields = '__all__'
        

