# This file sends emails from the default app
from django.core.mail import send_mail
from django.conf import settings

TEAM_NAME="HackTCNJ"
FROM_EMAIL= settings.EMAIL_OUTGOING

def test_mail():
    subject = "Testing mail"
    from_email=FROM_EMAIL
    body = '''
     Hey yo what's good dawg
    '''
    to_email = ['test@email.com']

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def password_reset_success(user):
    subject = "You've successfully reset your password!"
    from_email=FROM_EMAIL
    to_email = [user.email]
    body = '''
        Hey! You've successfully reset your password! 

        Thanks!
        {}
    '''.format(TEAM_NAME)

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def hacker_checkin_success(hacker):
    subject = "{}, you have checked in at HackTCNJ!".format(hacker.first_name)
    from_email=FROM_EMAIL
    to_email = [hacker.email]
    body = '''
    Hey {}, 

    Thanks for coming out this weekend to have a blast at HackTCNJ. We've checked you in to our system. 
    Please check out the website for the event schedule and we can't wait to see you at the opening ceremony!

    Best,
    
    '''.format(hacker.first_name, TEAM_NAME)


    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def new_organizer_added(organizer):
    subject = "{}, you have been added to HackTCNJ as an Organizer".format(
        organizer.first_name)
    from_email=FROM_EMAIL
    to_email = [organizer.email]
    body = '''
    Hey {}, 
        You've been added to the system as an organizer. You got some powers like checking in hackers.
        Your login credentials are associated with this email. You already know the password ;) 
        Please reset your password {}
   
        -{}
    '''.format(organizer.first_name, "add link here", TEAM_NAME)


    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def new_waitlister_added(email, name):
    subject = "Success! You've been added to the HackTCNJ Waiting List!"
    from_email=FROM_EMAIL
    to_email = [email]
    body = '''
    Hey {}, 
        We are totally pumped! HackTCNJ is coming soon! We can't wait for you to join us in celebrating another awesome year of hacking at The College of New Jersey!
        Once registration opens, we'll send you an email so you can sign up!

        Best,
        {}
    '''.format(name, TEAM_NAME)