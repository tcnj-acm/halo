import os
import json


from django.contrib.auth.models import User, Group
from default.models import CustomUser
from organizer.models import OrganizerInfo, WebsiteSettings, FeaturePermission, OrganizerPermission
from hacker.models import HackerInfo
from default.helper import add_group

def create_groups():
    Group.objects.create(name="hacker")
    Group.objects.create(name="organizer")
    Group.objects.create(name="head-organizer")
    Group.objects.create(name="checked-in")


permissions_list = []


def create_feature_permissions():
    permissions_list.append(FeaturePermission.objects.create(url_name='display-hackers', permission_name='h-Hackers'))
    permissions_list.append(FeaturePermission.objects.create(url_name='qr-checkin', permission_name='h-QR Checkin'))
    permissions_list.append(FeaturePermission.objects.create(url_name='manual-checkin', permission_name='h-Checkin'))
    permissions_list.append(FeaturePermission.objects.create(url_name='waiting-list', permission_name='w-Waiting List'))
    permissions_list.append(FeaturePermission.objects.create(url_name='edit-waiting-list', permission_name='w-Edit Waiting List'))
    permissions_list.append(FeaturePermission.objects.create(url_name='statistics', permission_name='s-Stats'))

def add_admin_group(email_input):
    admin_user = CustomUser.objects.get(email=email_input.strip())
    print(admin_user)
    add_group(admin_user, 'head-organizer')
    print("added to group")
    head_org = OrganizerPermission.objects.create(user=admin_user)
    head_org.permission.add(permissions_list[0], permissions_list[1], permissions_list[2], permissions_list[3], permissions_list[4], permissions_list[5])
    print("end of function")
def add_website_setting():
    WebsiteSettings.objects.create(waiting_list_status=False)

def main():
        
    email_input = input("Enter the email you used for creating the superuser: ")
    print("Running create_groups")
    create_groups()
    print("Finished creating groups. Creating permissions")
    create_feature_permissions()
    print("Finished creating groups. Adding admin to group with permissions")
    add_admin_group(email_input)
    print("Finished adding admin to group. Adding the website settings")
    add_website_setting()

main()