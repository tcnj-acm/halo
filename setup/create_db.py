# This python file creates 5 organizers, 21 hackers

# new_user = User.objects.create(username = row["email"], first_name= row["first"], last_name= row["last"], email = row["email"] + "@tcnj.edu")
#             new_user.set_password('tacos')
#             new_user.save()
from django.contrib.auth.models import User, Group
from default.models import CustomUser
from organizer.models import OrganizerInfo, WebsiteSettings, FeaturePermission, OrganizerPermission
from hacker.models import HackerInfo
from default.helper import add_group


# total count (make less than 30 for each for now)
TOTAL_ORGANIZERS = 5
TOTAL_HACKERS = 10


first_name_organizers = [
    'Abhi',
    'Kevin',
    'Sterly',
    'JM',
    'Tracy'
]

last_name_organizers = [
    'Vempati',
    'Williams',
    'Deracy',
    'JM',
    'McGrady'
]

email_organizers = [
    'abhi@aslan.com',
    'kevin@aslan.com',
    'sterly@aslan.com',
    'jm@aslan.com',
    'tracy@aslan.com'
]
address_organizers = [
    '2 Braemer Dr',
    '100 Primrose Cr',
    '10 Crabapple Ct',
    '5 Bellflower Ct',
    '6 Cranberry Ct'
]

###################################
###################################


first_name_hackers = [
    'Sophie',
    'Daryll',
    'Chandler',
    'Rachel',
    'Tony',
    'Jake',
    'Amy',
    'Raymond',
    'Mani',
    'Sabrina',
    'Brandon'
]

last_name_hackers = [
    'Goldberg',
    'Johnson',
    'Bing',
    'Green',
    'Stark',
    'Peralta',
    'Santiago',
    'Holt',
    'Yeluri',
    'May',
    'Kim'
]
email_hackers = [
    'sophie@tcnj.edu',
    'daryl@dm.com',
    'chandler@ps.com',
    'rachel@rl.com',
    'tony@mit.edu',
    'jake@b99.gov',
    'amy@b99.gov',
    'ray@b99.gov',
    'mani@tcnj.edu',
    'brandon@tcnj.edu'
]
address_hackers = [
    '56 Matawan Ln',
    '44 Scranton Rd',
    '120 46 W 10 Ave',
    '121 46 W 10 Ave',
    '1044 Malibu Pt',
    '33 Brooklyn Ln',
    '33 Brooklyn Ln',
    '60 Brooklyn Ln',
    '4 Galston Dr',
    '30 Pennington Rd',

]

majors = [
    'Accounting',
    'Biology',
    'Biomedical Engineering',
    'Business Administration',
    'Chemistry',
    'Civil Engineering',
    'Communications',
    'Computer Engineering',
    'Computer Science',
    'Construction Management',
    'Cybersecurity',
    'Economics',
    'Education',
    'Electronics Engineering',
    'English',
    'Finance',
    'Game Design',
    'Health Informatics',
    'Industrial Engineering',
    'Interactive Multimedia'
    'Information Technology',
    'Liberal Arts',
    'Management',
    'Management Information Systems',
    'Marketing',
    'Mechanical Engineering',
    'Nuclear Engineering',
    'Nursing',
    'Petroleum Engineering',
    'Physics',
    'Political Science',
    'Public Administration',
    'Software Engineering'
]

education_hackers = [
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "University (Undergrad)",
    "High School/Secondary School",
    "University (Undergrad)",
    "University (Undergrad)"
]

food_choices_hackers = [
    "Vegan",
    "Gluten-Free",
    "Vegetarian",
    "None",
    "None",
    "None",
    "Vegetarian",
    "Vegetarian",
    "None",
    "None",
]

shirt_sizes_hackers = [
    "Unisex (M)",
    "Unisex (M)",
    "Unisex (S)",
    "Unisex (S)",
    "Unisex (L)",
    "Unisex (L)",
    "Unisex (M)",
    "Unisex (M)",
    "Unisex (L)",
    "Unisex (L)",

]

# Create the necessary groups for the users


def create_groups():
    Group.objects.create(name="hacker")
    Group.objects.create(name="organizer")
    Group.objects.create(name="head-organizer")
    Group.objects.create(name="checked-in")


def create_super_user():
    CustomUser.objects.create_superuser('admin@aslan.com', 'hacker123!')


def create_users():

    for i in range(TOTAL_ORGANIZERS):
        new_user = CustomUser.objects.create(
            email=email_organizers[i], first_name=first_name_organizers[i], last_name=last_name_organizers[i], address=address_organizers[i])
        new_user.set_password('hacker123!')
        new_user.save()

    for i in range(TOTAL_HACKERS):
        new_user = CustomUser.objects.create(email=email_hackers[i], first_name=first_name_hackers[i], last_name=last_name_hackers[i],
                                             address=address_hackers[i], food_preference=food_choices_hackers[i], shirt_size=shirt_sizes_hackers[i])
        new_user.set_password('hacker123!')
        new_user.save()


def create_organizers():

    for i in range(TOTAL_ORGANIZERS):
        new_user = CustomUser.objects.get(email=email_organizers[i])
        new_org = OrganizerInfo.objects.create(user=new_user)
        add_group(new_user, 'organizer')


def create_hackers():
    for i in range(TOTAL_HACKERS):
        new_user = CustomUser.objects.get(email=email_hackers[i])
        new_hacker = HackerInfo.objects.create(
            user=new_user, major=majors[i], education=education_hackers[i])
        add_group(new_user, 'hacker')


def add_admin_to_group():
    admin_user = CustomUser.objects.get(email='admin@aslan.com')
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


def add_organizers_to_features():
    for i in range(TOTAL_ORGANIZERS):
        user = CustomUser.objects.get(email=email_organizers[i])
        org = OrganizerInfo.objects.get(user=user)

        org_perm = OrganizerPermission.objects.create(organizer=org)
        org_perm.permission.add(permissions_list[0], permissions_list[1],
                                permissions_list[2], permissions_list[3], permissions_list[4])


# Driver code
# site startup code
create_groups()
create_super_user()
create_users()
create_organizers()
create_hackers()

# admin startup code
'''
NOTE: Please run create_feature_permissions() together with add_organizers_to_features()
'''
add_admin_to_group()
add_website_setting()
create_feature_permissions()
add_organizers_to_features()
