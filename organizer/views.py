from email import message
from django.contrib import messages
from organizer.forms import OrganizerCreationForm, OrganizerPermissionControlForm
from django.db.models.query_utils import check_rel_lookup_compatibility, select_related_descend
from django.db.models import Count
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from hacker.models import HackerInfo
from .models import OrganizerInfo, OrganizerPermission, FeaturePermission, WebsiteSettings
from default.models import CustomUser, WaitingList
from default.helper import add_group, remove_group
from django.db.models import Q

from default.emailer import new_organizer_added


# Create your views here.


def dash(request):

    can_see_stats = OrganizerPermission.objects.filter(user = request.user, permission=FeaturePermission.objects.get(
        url_name='statistics')).exists()
    head_org = request.user.groups.filter(name='head-organizer').exists()
    context = {'head_org': head_org, 'can_see_stats': can_see_stats}
    return render(request, 'organizers/dashboard.html', context)


# All organizers can see hackers (all or those checked in)
def display_hackers(request):

    url_parameter = request.GET.get("q")
    if url_parameter:
        checked_in_hackers = HackerInfo.objects.filter(user__groups__name='checked-in').filter(
            Q(user__first_name__icontains=url_parameter) | Q(user__last_name__icontains=url_parameter) |
            Q(user__email__icontains=url_parameter)
        )
        nonchecked_in_hackers = HackerInfo.objects.exclude(user__groups__name='checked-in').filter(
            Q(user__first_name__icontains=url_parameter) | Q(user__last_name__icontains=url_parameter) |
            Q(user__email__icontains=url_parameter)
        )
    else:
        checked_in_hackers = HackerInfo.objects.filter(
            user__groups__name='checked-in')
        nonchecked_in_hackers = HackerInfo.objects.exclude(
            user__groups__name='checked-in')

    context = {'checked_in_hackers': checked_in_hackers,
               'nonchecked_in_hackers': nonchecked_in_hackers}
    return render(request, 'organizers/hackersdisplay.html', context)

# This is a view that shows people that are not checked in to the event
def manual_checkin(request):

    just_registered = None

    if request.method == 'POST':
        if 'undo-check-in-form' in request.POST:
            email = request.POST.get('email')
            hack = HackerInfo.objects.get(user__email=email)
            remove_group(hack.user, "checked-in")
        if "check-in-form" in request.POST:
            email = request.POST.get('email')
            hack = HackerInfo.objects.get(user__email=email)
            add_group(hack.user, "checked-in")
            just_registered = hack

    uncheckedin_hackers = HackerInfo.objects.exclude(
        user__groups__name='checked-in')

    context = {'uncheckedin_hackers': uncheckedin_hackers,
               'just_registered': just_registered}
    return render(request, 'organizers/manualcheckin.html', context)


# checkin view with qr code stuff
def qr_checkin(request, pk, first_name_hash, last_name_hash):

    hacker = HackerInfo.objects.get(user__id=pk)

    if request.method == 'POST':
        email = request.POST.get('email')
        hack = HackerInfo.objects.get(user__email=email)
        add_group(hack.user, "checked-in")
        return redirect('display-hackers')

    context = {'hacker': hacker}
    return render(request, 'organizers/qrcheckin.html', context)


# head organizer only function: show other organizers on the system
def display_organizers(request):

    all_organizers = OrganizerInfo.objects.all().exclude(
        user__email=request.user.email)
    context = {'all_organizers': all_organizers}
    return render(request, 'organizers/organizersdisplay.html', context)


# Head organizer only function: remove someone from the system.
def delete_organizer(request, id):
    selected_organizer = OrganizerInfo.objects.get(id=id)
    selected_user = selected_organizer.user

    selected_organizer.delete()
    selected_user.delete()

    context = {}
    return redirect('all-organizers')


# head organizer can add another organizer to the system
def add_organizer(request):
    create_organizer_form = OrganizerCreationForm()
    create_organizer_permission_form = OrganizerPermissionControlForm()
    if request.method == 'POST':
        new_organizer = OrganizerCreationForm(request.POST)
        organizer_permission = OrganizerPermissionControlForm(request.POST)
        if new_organizer.is_valid() and organizer_permission.is_valid():
            first_name = new_organizer.cleaned_data['first_name']
            last_name = new_organizer.cleaned_data['last_name']
            email = new_organizer.cleaned_data['email']
            passwrd = 'hacker123!'
            new_user = CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email)
            new_user.set_password(passwrd)
            
            
            add_group(new_user, 'organizer')
            new_user.save()

            org_perm_obj = organizer_permission.save(commit=False)
            org_perm_obj.user = new_user
            print(request.POST)
            org_perm_obj.save()
            organizer_permission.save_m2m()

            new_organizer = OrganizerInfo.objects.create(user=new_user)
            new_organizer.save()

            new_organizer_added(new_user)

            return redirect('all-organizers')
    context = {'create_organizer_form': create_organizer_form, 'create_organizer_permission_form':create_organizer_permission_form}
    return render(request, 'organizers/addorganizer.html', context)

def organizer_setting(request, pk):

    user = CustomUser.objects.get(id = pk)
    org_perm = OrganizerPermission.objects.get(user = user)
    form = OrganizerPermissionControlForm(instance=org_perm)
    
    if request.method == 'POST':
        form = OrganizerPermissionControlForm(request.POST, instance=org_perm)
        if form.is_valid():
            form.save()
            return redirect('all-organizers')

    context={'form':form, 'user':user}
    return render(request, 'organizers/editorganizer.html', context)

    

# head organizer settings page
def settings(request):
    current_setting = WebsiteSettings.objects.first()
    head_org = request.user.groups.filter(name='head-organizer').exists()
    if request.method == 'POST':
        value = request.POST.get('toggle-waitlist-control')
        if value == 'on' and current_setting.waiting_list_status == True:
            message = "Waiting List Status Unaffected"
        elif value == None and current_setting.waiting_list_status == False:
            message = "Waiting List Status Unaffected"
        else:
            if value == 'on':
                current_setting.waiting_list_status = True
                message = "Waiting List Activated"
                current_setting.save()
            else:
                current_setting.waiting_list_status = False
                message = "Waiting List Deactivated" 
                current_setting.save()
        messages.info(request, message)
    
    context = {'head_org':head_org, 'current_setting':current_setting}
    return render(request, 'organizers/websitesettings.html', context)


def stats_page(request):
    hacker_food = HackerInfo.objects.values_list('user__food_preference').annotate(fc=Count('user__food_preference')).order_by('-fc')
    hacker_major = HackerInfo.objects.values_list('major').annotate(fc=Count('major')).order_by('-fc')[:5]
    hacker_education = HackerInfo.objects.values_list('education').annotate(fc=Count('education')).order_by('-fc')
    waitlist_count = WaitingList.objects.all().count()
    register_count = HackerInfo.objects.all().count()
    checked_in_count = HackerInfo.objects.filter(user__groups__name='checked-in').count()
    context = { 'hacker_food':hacker_food,
                'hacker_major':hacker_major,
                'hacker_education':hacker_education,
                'waitlist_count':waitlist_count,
                'register_count':register_count,
                'checked_in_count':checked_in_count
    }
    return render(request, 'organizers/statspage.html', context)


def display_waitlist(request):
    waiting_list = WaitingList.objects.all()
    waitlist_count = waiting_list.count()
    waiting_list_emails = waiting_list.values_list('email')
    registered_hackers_emails = HackerInfo.objects.values_list('user__email')
    non_registered_count = waiting_list_emails.difference(registered_hackers_emails).count()
    
    
    context = { 'waitlist_count':waitlist_count,
                'waiting_list':waiting_list, 
                'non_registered_count':non_registered_count
    }
    return render(request, 'organizers/waitlistdisplay.html',context)
