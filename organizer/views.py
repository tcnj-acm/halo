from django.db.models.query_utils import select_related_descend
from django.shortcuts import render, redirect
from hacker.models import hacker
from .models import organizer
from django.db.models import Q

# Create your views here.


def dash(request):

    head_org = request.user.groups.filter(name='head-organizer').exists()
    context = {'head_org': head_org}
    return render(request, 'organizers/dashboard.html', context)


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


def display_organizer(request):

    all_organizers = organizer.objects.all().exclude(
        organizer__email=request.user.email)
    context = {'all_organizers': all_organizers}
    return render(request, 'organizers/organizerdisplay.html', context)


def delete_organizer(request, id):
    selected_organizer = organizer.objects.get(id=id)
    selected_user = selected_organizer.organizer

    selected_organizer.delete()
    selected_user.delete()

    context = {}
    return redirect('all-organizers')
