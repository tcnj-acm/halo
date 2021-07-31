from django.shortcuts import render

# Create your views here.

def dash(request):
    context = {}
    return render(request, 'organizers/dashboard.html', context)