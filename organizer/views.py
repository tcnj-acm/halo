from organizer.forms import NewOrganizer
from django.db.models.query_utils import select_related_descend
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from hacker.models import hacker
from .models import organizer
from default.models import CustomUser
from default.helper import add_group
from django.db.models import Q

from default.emailer import new_organizer_added
# Create your views here.


def dash(request):

    head_org = request.user.groups.filter(name='head-organizer').exists()
    context = {'head_org': head_org}
    return render(request, 'organizers/dashboard.html', context)


# All organizers can see hackers (all or those checked in)
def all_hackers(request):

    url_parameter = request.GET.get("q")
    if url_parameter:
        hackers_all = hacker.objects.filter(
            Q(hacker__first_name__icontains=url_parameter) | Q(hacker__last_name__icontains=url_parameter) |
            Q(hacker__email__icontains=url_parameter)
        )
    else:
        hackers_all = hacker.objects.all()

    context = {'hackers_all': hackers_all}
    return render(request, 'organizers/hackersdisplay.html', context)

# This is a view that shows people that are not checked in to the event


def registered_hackers(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        hack = CustomUser.objects.get(email=email)
        add_group(hack, "checked-in")



    uncheckedin_hackers = hacker.objects.exclude(
        hacker__groups__name='checked-in')

    context = {'uncheckedin_hackers': uncheckedin_hackers}
    return render(request, 'organizers/uncheckedinhackers.html', context)

# def checkin_hacker(request, hacker_user):


#     context = {}
#     return render(request, 'organizers/checkinhacker.html', context)

# head organizer only function: show other organizers on the system
def display_organizer(request):

    all_organizers = organizer.objects.all().exclude(
        organizer__email=request.user.email)
    context = {'all_organizers': all_organizers}
    return render(request, 'organizers/organizerdisplay.html', context)


# Head organizer only function: remove someone from the system.
def delete_organizer(request, id):
    selected_organizer = organizer.objects.get(id=id)
    selected_user = selected_organizer.organizer

    selected_organizer.delete()
    selected_user.delete()

    context = {}
    return redirect('all-organizers')


# head organizer can add another organizer to the system
def add_organizer(request):
    form = NewOrganizer()
    if request.method == 'POST':
        new_organizer = NewOrganizer(request.POST)
        if new_organizer.is_valid():
            fname = new_organizer.cleaned_data['fname']
            lname = new_organizer.cleaned_data['lname']
            email = new_organizer.cleaned_data['email']
            passwd = 'cistheworstlangever'
            new_user = CustomUser.objects.create(
                first_name=fname, last_name=lname, email=email)
            new_user.set_password(passwd)
            add_group(new_user, 'organizer')
            new_user.save()

            new_organizer = organizer.objects.create(organizer=new_user)
            new_organizer.save()

            new_organizer_added(new_user)
            return redirect('all-organizers')
    context = {'form': form}
    return render(request, 'organizers/addorganizer.html', context)
