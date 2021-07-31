from django.urls import path, re_path
from hacker import views 

urlpatterns = [

    path('hdash', views.dash, name='hacker-dash'),
]