from django.urls import path, re_path
from organizer import views

urlpatterns = [
     path('odash', views.dash, name='organizer-dash'),
     path('hackers', views.display_hackers, name='display-hackers'),
     path('minor-hackers', views.under18_hackers, name='under18-hackers'),
     path('download/', views.export_hacker_csv, name='export-hackers'),
     path('download-checkedin/', views.export_checkedin_hackers_csv, name='export-checkedin-hackers'),
     path('organizers', views.display_organizers, name='all-organizers'),
     path('organizers/delete/<int:id>',
          views.delete_organizer, name='delete-organizer'),
     path('organizers/add', views.add_organizer, name='add-organizer'),
     path('check-in', views.manual_checkin, name='manual-checkin'),
     path('check-in/<str:first_name_hash>/<str:last_name_hash>/<int:pk>',
          views.qr_checkin, name='qr-checkin'),
     path('waitlist', views.display_waitlist, name='waiting-list'),
     path('waitlist/edit', views.edit_waitlist, name='edit-waiting-list'),
     path('waitlist/delete/<int:pk>', views.delete_waitlist_participant, name='delete-waiting-list'),
     path('settings/', views.settings, name='website-settings'),
     path('stats/', views.stats_page, name='statistics'),
     path('organizers/edit/<int:pk>', views.organizer_setting, name='edit-organizer'),
     path('events/', views.events, name='manage-events')
]
