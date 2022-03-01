from email import message
import email
from multiprocessing import context
import re
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, HackerCreationForm, WaitingListCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
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
        create_user_form = CustomUserCreationForm(request.POST)
        create_hacker_form = HackerCreationForm(request.POST)
        
        if create_hacker_form.is_valid() and create_user_form.is_valid():
            pword = create_user_form.cleaned_data['password1']
            user = create_user_form.save()

            hacker = create_hacker_form.save(commit=False)
            hacker.user = user
            hacker.save()
            add_group(user, 'hacker')

            user = authenticate(request, username=user.email, password=pword)
            if user is not None:
                login(request, user)
                return redirect('hacker-dash') 
        else:
            print('fail')
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

            return redirect(decide_redirect(user))
        else:
            messages.error(request, "Username or Password Incorrect")

    context = {}
    return render(request, 'defaults/login.html', context)


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            user_email = password_reset_form.cleaned_data['email'].lower()
            user_obj_valid = CustomUser.objects.filter(email=user_email).exists()
            if user_obj_valid:
                user_obj = CustomUser.objects.get(email=user_email)
                uid = urlsafe_base64_encode(force_bytes(user_obj.pk))
                token = default_token_generator.make_token(user_obj)
                password_reset_instructions(request.get_host(), user_obj, uid, token)
                return redirect('password_reset_done')
            else:
                messages.error(request, "Email Could Not Be Found")
    password_reset_form = PasswordResetForm()

    context = {'password_reset_form':password_reset_form}
    return render(request, 'defaults/password_reset.html', context)



def logout_user(request):
    logout(request)
    return redirect('landing') 
