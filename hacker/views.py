from django.shortcuts import render, redirect
from .forms import *
from default.forms import CustomUserCreationForm

# Create your views here.

def dash(request):
    context = {}
    return render(request, 'hackers/dashboard.html', context)