from django.urls import path, re_path
from organizer import views

urlpatterns = [
    path('odash', views.dash, name='organizer-dash'),
    path('hackers', views.all_hackers, name='all-hackers'),
    path('organizers', views.display_organizer, name='all-organizers'),
    path('organizers-delete/<int:id>',views.delete_organizer, name='delete-organizer'),
    path('organizers-add', views.add_organizer, name='add-organizer'),
    path('uncheckedin-hackers', views.registered_hackers,name='registered-hackers'),
    path('checkin/<int:pk>', views.checkin_hacker, name='checkin-hacker'),
    path('checkedin-hackers', views.checkedin_hacker, name='checkedin-hackers'),


]
