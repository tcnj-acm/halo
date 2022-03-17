from django.shortcuts import render, redirect
from .models import HackerInfo
from default.forms import CustomUserCreationForm

import hashlib
# Create your views here.

def dash(request):

    hacker = HackerInfo.objects.get(user = request.user)
    first_name_hash = hashlib.sha256(hacker.user.first_name.encode()).hexdigest()
    last_name_hash = hashlib.sha256(hacker.user.last_name.encode()).hexdigest()

    check_in_url = "{}/check-in/{}/{}/{}".format(request.get_host(), first_name_hash,last_name_hash,hacker.user.id)
    context = {'check_in_url':check_in_url, 'hacker':hacker}
    return render(request, 'hackers/dashboard.html', context)