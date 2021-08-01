from django.urls import path, re_path
from default import views 

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register', views.register_hacker, name='hacker'),
    path('login', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]