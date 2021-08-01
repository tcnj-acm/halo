from django.shortcuts import render
from hacker.models import hacker
from django.db.models import Q
# Create your views here.


def dash(request):

    # If the user is head organizer
    # Display card to access django admin
    # Display card to access page of other organizers
    # is_head_organizer = user.groups.filter(name='head-organizer')
    context = {}
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
