# This python file creates 5 organizers, 21 hackers

# new_user = User.objects.create(username = row["email"], first_name= row["first"], last_name= row["last"], email = row["email"] + "@tcnj.edu")
#             new_user.set_password('tacos')
#             new_user.save()
from default.models import CustomUser
from organizer.models import organizer

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
def create_users():

    for i in range(5):
        new_user = CustomUser.objects.create(email = email_organizers[i], first_name=first_name_organizers[i], last_name = last_name_organizers[i])
        new_user.set_password('cistheworstlangever')
        new_user.save()

def create_organizers():

    for i in range(5):
        user = CustomUser.objects.get(email=email_organizers[i])
        new_org = organizer.objects.create(organizer=user, address=address_organizer[i])
    

create_users()
create_organizers()
