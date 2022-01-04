from organizer.forms import OrganizerCreationForm
from django.db.models.query_utils import check_rel_lookup_compatibility, select_related_descend
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from hacker.models import HackerInfo
from .models import OrganizerInfo
from default.models import CustomUser
from default.helper import add_group, remove_group
from django.db.models import Q

from default.emailer import new_organizer_added
# Create your views here.


def dash(request):

    head_org = request.user.groups.filter(name='head-organizer').exists()
    context = {'head_org': head_org}
    return render(request, 'organizers/dashboard.html', context)


# All organizers can see hackers (all or those checked in)
def display_hackers(request):

    url_parameter = request.GET.get("q")
    if url_parameter:
        all_hackers = hacker.objects.filter(
            Q(hacker__first_name__icontains=url_parameter) | Q(hacker__last_name__icontains=url_parameter) |
            Q(hacker__email__icontains=url_parameter)
        )
    else:
        all_hackers = hacker.objects.all()

    context = {'all_hackers': all_hackers}
    return render(request, 'organizers/hackersdisplay.html', context)



# This is a view that shows people that are not checked in to the event
def manual_checkin(request):

    just_registered = None

    if request.method == 'POST':
        if 'undo-check-in-form' in request.POST:
            email = request.POST.get('email')
            hack = hacker.objects.get(hacker__email=email)
            remove_group(hack.hacker, "checked-in")
        if "check-in-form" in request.POST:
            email = request.POST.get('email')
            hack = hacker.objects.get(hacker__email=email)
            add_group(hack.hacker, "checked-in")
            just_registered = hack

    uncheckedin_hackers = hacker.objects.exclude(
        hacker__groups__name='checked-in')

    context = {'uncheckedin_hackers': uncheckedin_hackers, 'just_registered':just_registered}
    return render(request, 'organizers/manualcheckin.html', context)


# head organizer only function: show other organizers on the system
def display_organizers(request):

    all_organizers = OrganizerInfo.objects.all().exclude(
        OrganizerInfo__email=request.user.email)
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
    if request.method == 'POST':
        new_organizer = NewOrganizer(request.POST)
        if new_organizer.is_valid():
            first_name = new_organizer.cleaned_data['fname']
            last_name = new_organizer.cleaned_data['lname']
            email = new_organizer.cleaned_data['email']
            passwrd = 'hacker123!'
            new_user = CustomUser.objects.create(
                first_name=first_name, last_name=last_name, email=email)
            new_user.set_password(passwrd)
            add_group(new_user, 'organizer')
            new_user.save()

            new_organizer = OrganizerInfo.objects.create(uesr=new_user)
            new_organizer.save()

            new_organizer_added(new_user)
            return redirect('all-organizers')
    context = {'create_organizer_form': create_organizer_form}
    return render(request, 'organizers/addorganizer.html', context)
