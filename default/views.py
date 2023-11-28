from email import message
import email
from multiprocessing import context
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import json
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, HackerCreationForm, WaitingListCreationForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from hacker.models import HackerInfo
from organizer.models import OrganizerInfo
from .helper import add_group, decide_redirect, decide_type
from .emailer import *
from .models import WaitingList, CustomUser
from sendgrid import SendGridAPIClient
from halo.settings.dev import SENDGRID_API_KEY


def landing(request):
    if request.method == "POST":
        waitlist_create_form = WaitingListCreationForm(request.POST)
        if waitlist_create_form.is_valid():
            waitlist = waitlist_create_form.save()
            new_email = waitlist_create_form.cleaned_data['email']
            new_name = waitlist_create_form.cleaned_data['full_name']
            new_waitlister_added(new_email, new_name)
            fname = new_name.split(' ')[0]
            
            if len(new_name.split(' ')) == 1:
                lname = ''
            else:
                lname = new_name.split(' ')[1]
            add_user_to_mailing_list(fname, lname, new_email)
            messages.success(
                request, "Thanks for joining the waiting list, you will receive an email with more information soon!")
            return redirect('landing')
    else:
        # sg = SendGridAPIClient(os.getenv('EM_HOST_PASSWORD'))
        # params = {'page_size': 100}

        # response = sg.client.marketing.lists.get(
        #     query_params=params
        # )
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        waitlist_create_form = WaitingListCreationForm()
    context = {'waitlist_form': waitlist_create_form}
    return render(request, 'defaults/landing.html', context)


def waitlist(request):
    # fundraiser_link = request.get_host() + "/fundraiser"
    if request.method == "POST":
        waitlist_create_form = WaitingListCreationForm(request.POST)
        if waitlist_create_form.is_valid():
            waitlist = waitlist_create_form.save()
            new_email = waitlist_create_form.cleaned_data['email']
            new_name = waitlist_create_form.cleaned_data['full_name']
            new_waitlister_added(new_email, new_name)
            messages.success(
                request, "Thanks for joining the waiting list, you will receive an email with more information soon!")
            return redirect('waitlist')
    else:
        waitlist_create_form = WaitingListCreationForm()

    context = {'waitlist_form': waitlist_create_form}
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

            phone = request.POST.get('phone')
            user.phone = phone

            if address2 == "":
                address = address1 + ", " + city + ", " + state + ", " + zip + ", " + country
            else:
                address = address1 + ", " + address2 + ", " + \
                    city + ", " + state + ", " + zip + ", " + country

            user.address = address

            email = create_user_form.cleaned_data['email'].lower()
            user = create_user_form.save(commit=False)
            user.email = email

            user.save()

            hacker = create_hacker_form.save(commit=False)
            hacker.user = user
            hacker.save()
            add_group(user, 'hacker')

            # Email confirmation
            registration_confirmation(user)
            add_user_to_mailing_list(
                user.first_name, user.last_name, user.email)

            if user.age < 18:
                link = request.get_host() + "/waiver"
                minor_waiver_form_submission(user, link)

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

    context = {'create_hacker_form': create_hacker_form,
               'create_user_form': create_user_form}
    return render(request, 'defaults/register.html', context)


def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email').lower()
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
            user_obj_valid = CustomUser.objects.filter(
                email=user_email).exists()
            if user_obj_valid:
                user_obj = CustomUser.objects.get(email=user_email)
                uid = urlsafe_base64_encode(force_bytes(user_obj.pk))
                token = default_token_generator.make_token(user_obj)
                password_reset_instructions(
                    request.get_host(), user_obj, uid, token)
                return redirect('password_reset_done')
            else:
                messages.error(request, "Email Could Not Be Found")
    password_reset_form = PasswordResetForm()

    context = {'password_reset_form': password_reset_form}
    return render(request, 'defaults/password_reset.html', context)


def logout_user(request):
    logout(request)

    return redirect('landing')  # TODO


def check_email(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        received_json = json.loads(body_unicode)
        data = received_json.get("data")
        email_value = data.get("email").lower()
        message = ""
        validity = True
        if (CustomUser.objects.filter(email=email_value).exists()):
            message = "This Email is Already Registered"
            validity = False
        data = {
            "valid": validity,
            "message": message
        }
        return JsonResponse(data)

    return JsonResponse({"valid": False}, status=200)


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
                "valid": False,
                "errors": list(e)
            }
            return JsonResponse(data)

        data = {
            "valid": True,
            "errors": ""
        }
        return JsonResponse(data)
    return JsonResponse({"valid": False}, status=200)

    return redirect('landing')


def fundraiser_link(request):

    context = {}
    return render(request, 'defaults/fundraiser.html', context)


def minor_waiver_form(request):

    context = {}
    return render(request, 'defaults/minor_waiver.html', context)


def profile_page(request, pk):
    user = None
    try:
        user = CustomUser.objects.get(id=pk)
        # print(user)
        # print(request.user)
    except:
        return redirect(decide_redirect(request.user))

    if user != request.user:
        # print("redirecting")
        return redirect(decide_redirect(request.user))

    is_hacker = True if decide_type(user) == "hacker" else False

    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=user)
        if user_change_form.is_valid():
            # print("valid")
            user_change_form.save()
            messages.success(request, "Profile updated!")
            return redirect('profile', pk=user.id)
    user_change_form = CustomUserChangeForm(instance=user)

    context = {"user_change_form": user_change_form}
    if is_hacker:
        return render(request, 'defaults/profileH.html', context)
    return render(request, 'defaults/profileO.html', context)
