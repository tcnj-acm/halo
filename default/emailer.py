# This file sends emails from the default app
from django.core.mail import send_mail


from_email = 'messanger@localhost.com'


def test_mail():
    subject = "Testing mail"
    body = '''
     Hey yo what's good dawg
    '''
    to_email = ['test@email.com']

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def password_reset_success(user):
    subject = "You've successfully reset your password!"

    to_email = [user.email]
    body = '''
        Hey! You've successfully reset your password! 

        Thanks!
        <Insert team name here>
    '''

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def hacker_checkin_success(hacker):
    subject = "{}, you have checked in at HackTCNJ!".format(hacker.first_name)
    body = '''
    Hey {}, 

    Thanks for coming out this weekend to have a blast at HackTCNJ. We've checked you in to our system. 
    Please check out the website for the event schedule and we can't wait to see you at the opening ceremony!
    '''.format(hacker.first_name)

    to_email = [hacker.email]

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def new_organizer_added(organizer):
    subject = "{}, you have been added to HackTCNJ as an Organizer".format(
        organizer.first_name)
    body = '''
    Hey {}, 
        You've been added to Aslan as an organizer. You got some powers like checking in hackers
        And viewing hackers data. Please reset your password here. 
   
    '''.format(organizer.first_name)

    to_email = [organizer.email]

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)
