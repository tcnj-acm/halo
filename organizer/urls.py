from django.urls import path, re_path
from organizer import views

urlpatterns = [
    path('odash', views.dash, name='organizer-dash'),
    path('hackers', views.all_hackers, name='all-hackers'),
]
