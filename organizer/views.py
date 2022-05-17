from email import message
from multiprocessing import Event
from django.contrib import messages
from organizer.forms import OrganizerCreationForm, OrganizerPermissionControlForm
from django.http import HttpResponse
from django.db.models.query_utils import check_rel_lookup_compatibility, select_related_descend
from django.db.models import Count
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from hacker.models import HackerInfo
from .models import OrganizerInfo, OrganizerPermission, FeaturePermission, WebsiteSettings
from default.models import CustomUser, WaitingList, Event
from default.helper import add_group, remove_group
from django.db.models import Q
from django.db.models import Value as V
from django.db.models.functions import Concat  
from .helper import get_permissions
from default.emailer import new_organizer_added, add_user_to_mailing_list
from default.forms import EventCreationForm
from .utils import download_csv

# Create your views here.




def dash(request):
    head_org = request.user.groups.filter(name='head-organizer').exists()

    context = {'head_org': head_org, 'permissions':get_permissions(request.user)}
    return render(request, 'organizers/dashboard.html', context)


# All organizers can see hackers (all or those checked in)
def display_hackers(request):

    url_parameter = request.GET.get("q")
    if url_parameter:
        checked_in_hackers = HackerInfo.objects.filter(user__groups__name='checked-in').filter(
            Q(user__first_name__icontains=url_parameter) | Q(user__last_name__icontains=url_parameter) |
            Q(user__email__icontains=url_parameter) | Q(user__registration_comment__icontains=url_parameter)
        )
        nonchecked_in_hackers = HackerInfo.objects.exclude(user__groups__name='checked-in').filter(
            Q(user__first_name__icontains=url_parameter) | Q(user__last_name__icontains=url_parameter) |
            Q(user__email__icontains=url_parameter) | Q(user__registration_comment__icontains=url_parameter)
        )
    else:
        checked_in_hackers = HackerInfo.objects.filter(
            user__groups__name='checked-in')
        nonchecked_in_hackers = HackerInfo.objects.exclude(
            user__groups__name='checked-in')

    context = { 'checked_in_hackers': checked_in_hackers,
                'nonchecked_in_hackers': nonchecked_in_hackers,
                'permissions':get_permissions(request.user)
               }
    return render(request, 'organizers/hackersdisplay.html', context)

def under18_hackers(request):
    url_parameter = request.GET.get("q")

    young_hackers = HackerInfo.objects.filter(user__age__lt=18)
    
    context = {'young_hackers':young_hackers}
    return render(request, 'organizers/minorhackers.html', context)


def export_hacker_csv(request):
  # Create the HttpResponse object with the appropriate CSV header.
#   id;password;date_joined;last_login;is_admin;is_active;is_staff;is_superuser;food_preference;resume;registration_comment;groups;user_permissions
# email;first_name;last_name;address;;shirt_size;gender;age;school_name;level_of_study;major
#   query = CustomUser.objects.defer('id', 'password', 'date_joined', 'last_login', 'is_admin', 'is_active','is_staff', 'is_superuser', 'food_preference','resume', 'groups', 'user_permissions', 'registration_comment').only('email','first_name','last_name','address','shirt_size','gender','age','school_name','level_of_study','major')
  
#   id;password;date_joined;last_login;is_admin;is_active;is_staff;is_superuser;email;first_name;last_name;address;food_preference;shirt_size;gender;age;school_name;level_of_study;major;resume;registration_comment;groups;user_permissions
#   query = CustomUser.objects.only('email','first_name','last_name','address','shirt_size','gender','age','school_name','level_of_study','major')
  data = download_csv(request, CustomUser.objects.only('email','first_name','last_name','address','shirt_size','gender','age','school_name','level_of_study','major'))
  response = HttpResponse(data, content_type='text/csv')
  return response

def export_checkedin_hackers_csv(request):
    data = download_csv(request, CustomUser.objects.filter(groups__name='checked-in').only('email','first_name','last_name','address','shirt_size','gender','age','school_name','level_of_study','major'))
    response = HttpResponse(data, content_type='text/csv')
    return response

# This is a view that shows people that are not checked in to the event
def manual_checkin(request):

    just_registered = None
    nonchecked_in_hackers = None
    url_parameter = request.GET.get("q")
    if url_parameter:
        nonchecked_in_hackers = HackerInfo.objects.exclude(user__groups__name='checked-in').filter(
            Q(user__first_name__icontains=url_parameter) | Q(user__last_name__icontains=url_parameter) |
            Q(user__email__icontains=url_parameter)
        )
    else:
        nonchecked_in_hackers = HackerInfo.objects.exclude(user__groups__name='checked-in')

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


    context = {'uncheckedin_hackers': nonchecked_in_hackers,
               'just_registered': just_registered,
                'permissions':get_permissions(request.user)
               }
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
    context = {'all_organizers': all_organizers,
                'permissions':get_permissions(request.user)
                }
    return render(request, 'organizers/organizersdisplay.html', context)


# Head organizer only function: remove someone from the system.
def delete_organizer(request, id):
    selected_organizer = OrganizerInfo.objects.get(id=id)
    selected_user = selected_organizer.user

    selected_organizer.delete()
    selected_user.delete()

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
            
            # print(request.POST)
            
            org_perm_obj.save()
            organizer_permission.save_m2m()

            new_organizer = OrganizerInfo.objects.create(user=new_user)
            new_organizer.save()

            reset_link = request.get_host() + "/reset-password"
            new_organizer_added(reset_link, new_user)
            add_user_to_mailing_list(new_user.first_name, new_user.last_name, new_user.email)

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

    context={'form':form, 'user':user,  'permissions':get_permissions(request.user)}
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
    
    context = {'head_org':head_org, 'current_setting':current_setting, 'permissions':get_permissions(request.user)}
    return render(request, 'organizers/websitesettings.html', context)


def stats_page(request):
    hacker_food = CustomUser.objects.values_list('food_preference').annotate(fc=Count('food_preference')).order_by('-fc')
    hacker_major = CustomUser.objects.values_list('major').annotate(fc=Count('major')).order_by('-fc')[:5]
    hacker_education = CustomUser.objects.values_list('level_of_study').annotate(fc=Count('level_of_study')).order_by('-fc')
    hacker_shirts = CustomUser.objects.values_list('shirt_size').annotate(fc=Count('shirt_size'))
    waitlist_count = WaitingList.objects.all().count()
    register_count = HackerInfo.objects.all().count()
    checked_in_count = HackerInfo.objects.filter(user__groups__name='checked-in').count()

    checked_hacker_food = CustomUser.objects.filter(groups__name='checked-in').values_list('food_preference').annotate(fc=Count('food_preference')).order_by('-fc')
    checked_hacker_major = CustomUser.objects.filter(groups__name='checked-in').values_list('major').annotate(fc=Count('major')).order_by('-fc')[:5]
    checked_hacker_education = CustomUser.objects.filter(groups__name='checked-in').values_list('level_of_study').annotate(fc=Count('level_of_study')).order_by('-fc')
    checked_hacker_shirts = CustomUser.objects.filter(groups__name='checked-in').values_list('shirt_size').annotate(fc=Count('shirt_size'))

    context = { 'hacker_food':hacker_food,
                'hacker_major':hacker_major,
                'hacker_education':hacker_education,
                'waitlist_count':waitlist_count,
                'register_count':register_count,
                'checked_in_count':checked_in_count,
                'hacker_shirts':hacker_shirts,
                'checked_hacker_food':checked_hacker_food,
                'checked_hacker_major':checked_hacker_major,
                'checked_hacker_education':checked_hacker_education,
                'checked_hacker_shirts':checked_hacker_shirts,
                'permissions':get_permissions(request.user)
    }
    return render(request, 'organizers/statspage.html', context)


def display_waitlist(request):
    waiting_list = WaitingList.objects.all()
    waitlist_count = waiting_list.count()
    waiting_list_emails = waiting_list.values_list('email')
    registered_hackers_emails = HackerInfo.objects.values_list('user__email')
    non_registered_count = waiting_list_emails.difference(registered_hackers_emails).count()
    
    waiting_list_values = waiting_list.annotate(status=V('non-reg')).values_list('email', 'full_name','status')
    registered_hackers_values = HackerInfo.objects.annotate(full_name=Concat('user__first_name',V(' ') ,'user__last_name'), status=V('reg')).values_list('user__email', 'full_name','status')
    waiting_list_intersect_registered = waiting_list_values.intersection(registered_hackers_values)
    waiting_list_minus_registered = waiting_list_values.difference(registered_hackers_values)

    all_waiting_list = waiting_list_intersect_registered.union(waiting_list_minus_registered).order_by('email')
    
    context = { 'waitlist_count':waitlist_count,
                'non_registered_count':non_registered_count,
                'permissions':get_permissions(request.user),
                'all_waiting_list':all_waiting_list,
    }
    return render(request, 'organizers/waitlistdisplay.html',context)

def edit_waitlist(request):
    waiting_list = WaitingList.objects.all()
    waitlist_count = waiting_list.count()
    waiting_list_emails = waiting_list.values_list('email')
    registered_hackers_emails = HackerInfo.objects.values_list('user__email')
    non_registered_count = waiting_list_emails.difference(registered_hackers_emails).count()
    
    
    context = { 'waitlist_count':waitlist_count,
                'waiting_list':waiting_list, 
                'non_registered_count':non_registered_count,
                'permissions':get_permissions(request.user)
    }
    return render(request, 'organizers/editwaitlist.html',context)

def delete_waitlist_participant(request, pk):
    participant = WaitingList.objects.get(id = pk)
    participant.delete()

    return redirect('edit-waiting-list')

def events(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            event = form.save()
    else:
        form = EventCreationForm()


    all_events = Event.objects.all()
    context = {'events':all_events, 'form':form}
    return render(request, 'organizers/events.html', context)
    