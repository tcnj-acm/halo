from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, HackerCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetCompleteView
from hacker.models import HackerInfo
from organizer.models import OrganizerInfo
from .helper import add_group, decide_redirect
from .emailer import *


def landing(request):

    context = {}
    return render(request, 'defaults/landing.html', context)


def registration(request):
    if request.method == 'POST':
        create_user_form = CustomUserCreationForm(request.POST)
        create_hacker_form = HackerCreationForm(request.POST)

        # print("in thingy")
        
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
                return redirect('hacker-dash') #TODO
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
            print(user)
            login(request, user)

            return redirect(decide_redirect(user)) #TODO
        else:
            HttpResponse("Username or Password Incorrect")

    context = {}
    return render(request, 'defaults/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing') #TODO
