from email import message
import re
from xml.dom import ValidationErr
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import json
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, HackerCreationForm, WaitingListCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from hacker.models import HackerInfo
from organizer.models import OrganizerInfo
from .helper import add_group, decide_redirect
from .emailer import *
from .models import WaitingList, CustomUser


def landing(request):
    context = {}
    return render(request, 'defaults/landing.html', context)

def waitlist(request):

    if request.method == "POST":
        waitlist_create_form = WaitingListCreationForm(request.POST)
        if waitlist_create_form.is_valid():
            waitlist = waitlist_create_form.save()
            new_email = waitlist_create_form.cleaned_data['email']
            new_name = waitlist_create_form.cleaned_data['full_name']
            new_waitlister_added(new_email, new_name)
            messages.success(request, "Thanks for joining the waiting list! You will recieve an email with more information soon!")
            return redirect('waitlist')
    else:
        waitlist_create_form = WaitingListCreationForm()
    
    
    context = {'waitlist_form':waitlist_create_form}
    return render(request, 'defaults/coming-soon.html', context)

def registration(request):
    if request.method == 'POST':
        create_user_form = CustomUserCreationForm(request.POST, request.FILES)
        create_hacker_form = HackerCreationForm(request.POST)
        
        if create_hacker_form.is_valid() and create_user_form.is_valid():
            pword = create_user_form.cleaned_data['password1']
            user = create_user_form.save()
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip = request.POST.get('zip')
            country = request.POST.get('country')

            if address2 == "":
                address = address1 + ", " + city + ", " + state + ", " + zip + ", " + country
            else:
                address = address1 + ", " + address2 + ", " + city + ", " + state + ", " + zip + ", " + country

            user.address = address
            user.save()

            hacker = create_hacker_form.save(commit=False)
            hacker.user = user
            hacker.save()
            add_group(user, 'hacker')

            # Email confirmation
            registration_confirmation(user)
            
            if user.age < 18:
                minor_waiver_form_submission(user)

            user = authenticate(request, username=user.email, password=pword)
            if user is not None:
                login(request, user)
                return redirect('hacker-dash')
        else:
            # print('fail')
            pass
    else:
        create_user_form = CustomUserCreationForm()
        create_hacker_form = HackerCreationForm()


    context = {'create_hacker_form': create_hacker_form, 'create_user_form': create_user_form}
    return render(request, 'defaults/register.html', context)



def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        passwrd = request.POST.get('password')

        user = authenticate(request, email=email, password=passwrd)

        if user is not None:
            login(request, user)

            return redirect(decide_redirect(user)) #TODO
        else:
            messages.error(request, "Username or Password Incorrect")

    context = {}
    return render(request, 'defaults/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing') #TODO


def check_email(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        data = received_json.get("data")
        email_value = data.get("email").lower()
        message = ""
        validity = True
        if(CustomUser.objects.filter(email=email_value).exists()):
            message = "This Email is Already Registered"
            validity = False
        data = {
            "valid":validity,
            "message":message
        }
        return JsonResponse(data)

    return JsonResponse({"valid":False}, status = 200)

def check_password(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        data = received_json.get("data")
        password_value = data.get("p1")
        try:
            validate_password(password_value)
        except ValidationError as e:
            data = {
                "valid":False,
                "errors":list(e)
            }
            return JsonResponse(data)


        data = {
            "valid":True,
            "errors":""
        }  
        return JsonResponse(data)
    return JsonResponse({"valid":False}, status = 200)
