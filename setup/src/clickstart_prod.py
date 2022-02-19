from django.contrib.auth.models import User, Group
from default.models import CustomUser
from default.helper import add_group

def create_groups():
    Group.objects.create(name="hacker")
    Group.objects.create(name="organizer")
    Group.objects.create(name="head-organizer")
    Group.objects.create(name="checked-in")


def add_admin_group():
    admin_user = CustomUser.objects.get(email='vempata1@tcnj.edu')
    add_group(admin_user, 'head-organizer')

def add_website_setting():
    WebsiteSettings.objects.create(waiting_list_status=False)


permissions_list = []


def create_feature_permissions():
    permissions_list.append(FeaturePermission.objects.create(
        url_name='display-hackers', permission_name='h-hackers'))
    permissions_list.append(
        FeaturePermission.objects.create(url_name='qr_checkin', permission_name='h-QR Checkin'))
    permissions_list.append(FeaturePermission.objects.create(
        url_name='manual_checkin', permission_name='h-Checkin'))
    permissions_list.append(FeaturePermission.objects.create(
        url_name='waiting-list', permission_name='w-Waiting List'))
    permissions_list.append(FeaturePermission.objects.create(
        url_name='edit-waiting-list', permission_name='w-Edit Waiting List'))
    permissions_list.append(FeaturePermission.objects.create(
        url_name='statistics', permission_name='s-Stats'))

create_groups()
add_admin_group()
add_website_setting()
create_feature_permissions()
