# This file sends emails from the default app
from django.core.mail import send_mail
from django.template.loader import render_to_string
from aslan.settings.base import EMAIL_OUTGOING
import re
TEAM_NAME="Team HackTCNJ"
FROM_EMAIL= EMAIL_OUTGOING

def test_mail():
    subject = "Testing mail"
    from_email=FROM_EMAIL
    body = '''
     Hey yo what's good dawg
    '''
    to_email = ['abhijitvempati@gmail.com']

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def password_reset_instructions(domain, user, uid, token):
    subject = "HackTCNJ Reset Password Link"
    from_email=FROM_EMAIL
    to_email=[user.email]
    email_variables = {
        "domain":domain,
        "uid": uid,  
        "user": user,
        "token": token,
        "team_name":TEAM_NAME,
    }


    body = render_to_string('defaults/resetpassword.txt', email_variables)

    send_mail(subject=subject, from_email=from_email, 
                recipient_list=to_email, message=body,fail_silently=False)

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

def registration_confirmation(hacker):
    subject = "{}, you've successfully registered for HackTCNJ (YAY!)".format(hacker.first_name)
    from_email=FROM_EMAIL
    to_email=[hacker.email]
    body = '''
        Hey {},

        We've received your hacker application for HackTCNJ! We can't wait to see you at TCNJ on April 9th, 2022. 
        You'll receive emails from us regarding check-in information and some logistics. 


        See you there! 
        {}
    '''.format(hacker.first_name,TEAM_NAME)

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)


def minor_waiver_form_submission(hacker):
    subject = "{}, you've successfully registered for HackTCNJ (YAY!)".format(hacker.first_name)
    from_email=FROM_EMAIL
    to_email=[hacker.email]
    body = '''
        Hey {},

        Thanks again for registering for the HackTCNJ. We require all minors (under 18), to bring a signed waiver form by your primary care taker.
        You will not be able to check in to the event without it. 

        You'll receive an email with a link to the form soon. 
        Thanks for working with us! 

        Best, 

        {}
    '''.format(hacker.first_name,"LINK", TEAM_NAME)

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


def new_organizer_added(link, organizer):
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
    '''.format(organizer.first_name, link, TEAM_NAME)


    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)

def new_waitlister_added(email, name, link):
    subject = "HackTCNJ Waiting List Success! Secure Some Cool Swag!"
    from_email=FROM_EMAIL
    to_email = [email]
    body = '''
    Hey {}, 
        We are totally pumped! HackTCNJ is coming soon! We can't wait for you to join us in celebrating another awesome year of hacking at The College of New Jersey!
        Once registration opens, we'll send you an email so you can sign up!

        This will be our first in-person Hackathon since the pandemic! We're raising money to help support the event, and to help spread our new designs for this year's logo! We are selling unique, limited time merchandise!
        The shirts will be delivered before the hackathon so you can rep a unique, awesome shirt! To join the awesome list, purchase a shirt or sweater from our customink fundraiser here:

        {}

        Best,
        {}
    '''.format(name, link, TEAM_NAME)

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)