# This python file creates 5 organizers, 21 hackers

# new_user = User.objects.create(username = row["email"], first_name= row["first"], last_name= row["last"], email = row["email"] + "@tcnj.edu")
#             new_user.set_password('tacos')
#             new_user.save()
from django.contrib.auth.models import User, Group
from default.models import CustomUser
from organizer.models import organizer
from hacker.models import hacker
from default.helper import add_group

# total count
TOTAL_ORGANIZERS = 5
TOTAL_HACKERS = 10

# Create the necessary groups for the users
Group.objects.create(name="hacker")
Group.objects.create(name="organizer")


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
address_organizer = [
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

major_hackers = [
    'Computer Science',
    'Civil Engineering',
    'Accounting',
    'Communications',
    'Computer Engineering',
    'Computer Science',
    'Arts History',
    'Architectural Design',
    'Computer Science',
    'Computer Science',

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
def create_users():

    for i in range(TOTAL_ORGANIZERS):
        new_user = CustomUser.objects.create(email = email_organizers[i], first_name=first_name_organizers[i], last_name = last_name_organizers[i])
        new_user.set_password('cistheworstlangever')
        new_user.save()

def create_organizers():

    for i in range(TOTAL_ORGANIZERS):
        user = CustomUser.objects.get(email=email_organizers[i])
        new_org = organizer.objects.create(organizer=user, address=address_organizer[i])
        add_group(user, 'organizer')    


def create_hackers():
    for i in range(TOTAL_HACKERS):
        new_user = CustomUser.objects.create(email=email_hackers[i], first_name=first_name_hackers[i], last_name=last_name_hackers[i])
        new_user.set_password('hacker123!')
        new_user.save()

        new_hacker = hacker.objects.create(hacker=new_user,address = address_hackers[i], major=major_hackers[i], education=education_hackers[i],food_preference=food_choices_hackers[i], shirt_size=shirt_sizes_hackers[i])
        add_group(new_user, 'hacker')


# Driver code
create_users()
create_organizers()
create_hackers()

