from django.urls import path, re_path
from organizer import views

urlpatterns = [
    path('odash', views.dash, name='organizer-dash'),
    path('hackers', views.display_hackers, name='display-hackers'),
    path('organizers', views.display_organizers, name='all-organizers'),
    path('organizers/delete/<int:id>',
         views.delete_organizer, name='delete-organizer'),
    path('organizers/add', views.add_organizer, name='add-organizer'),
    path('check-in', views.manual_checkin, name='manual-checkin'),
    path('check-in/<str:first_name_hash>/<str:last_name_hash>/<int:pk>',
         views.qr_checkin, name='qr-checkin'),
    path('settings/', views.settings, name='website-settings'),
    path('stats/', views.stats_page, name='statistics'),


]
