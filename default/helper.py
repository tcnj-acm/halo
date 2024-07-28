from django.contrib.auth.models import User, Group
from hacker.models import HackerInfo
from organizer.models import OrganizerInfo



def decide_redirect(user):
    if user.groups.filter(name='hacker').exists(): 
        return "hacker-dash"
    elif user.groups.filter(name='organizer').exists(): 
        return "organizer-dash"
    else:
        return "organizer-dash"

    # if hacker.objects.filter(hacker__email=user.email).exists():
    #     return "hacker-dash"
    # if organizer.objects.filter(organizer__email=user.email).exists():
    #     return "organizer-dash"
    # if sponsor.objects.filter(organizer__email=user.email).exists():
    #     return "organizer-dash"


def decide_type(user):
    if user.groups.filter(name='hacker').exists(): 
        return "hacker"
    elif user.groups.filter(name='organizer').exists(): 
        return "organizer"
    else:
        return "head-organizer"
    # if hacker.objects.filter(hacker__email=user.email).exists():
    #     return "hacker"
    # if organizer.objects.filter(organizer__email=user.email).exists():
    #     return "organizer"
    # if sponsor.objects.filter(organizer__email=user.email).exists():
    #     return "sponsor"

def add_group(user, group_name):
    user.groups.add(Group.objects.get(name=group_name))

def remove_group(user, group_name):
    user.groups.remove(Group.objects.get(name=group_name))