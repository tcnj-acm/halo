# This file sends emails from the default app
from django.core.mail import send_mail
from django.template.loader import render_to_string
from halo.settings.base import EMAIL_OUTGOING
from .models import WaitingList
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os
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

        We've received your hacker application for HackTCNJ! We can't wait to see you at TCNJ on February 17th, 2024. 
        You'll receive emails from us regarding check-in information and some logistics. 


        See you there! 
        {}
    '''.format(hacker.first_name,TEAM_NAME)

    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=body, fail_silently=False)

def minor_waiver_form_submission(hacker, link):
    subject = "{}, HackTCNJ Minor Waiver Form".format(hacker.first_name)
    from_email=FROM_EMAIL
    to_email=[hacker.email]
    body = '''
        Hey {},

        Thanks again for registering for the HackTCNJ. We require all minors (under 18), to bring a signed waiver form by your primary care taker.
        You will not be able to check in to the event without it. 

        Link to form: {}
        Thanks for working with us! 

        Best, 

        {}
    '''.format(hacker.first_name, link, TEAM_NAME)

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
    body = '''Hey {},
    
    You've been added to the system as an organizer. You got some powers like checking in hackers.
    Your login credentials are associated with this email. You already know the password ;) 
    
    Please reset your password {}
   
-{}
    '''.format(organizer.first_name, link, TEAM_NAME)


    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=body, fail_silently=False)

def new_waitlister_added(email, name):
    subject = "HackTCNJ Mailing List Success! Registration Opens Soon!"
    from_email=FROM_EMAIL
    to_email = [email]
    body = '''
Hey {}, 
    
    \tWe are totally pumped! HackTCNJ is coming soon! We can't wait for you to join us in celebrating another awesome year of hacking at The College of New Jersey!
    
    \tOnce registration opens, we'll send you an email so you can sign up!


Best,
{}
    '''.format(name, TEAM_NAME)

    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=body, fail_silently=False)
    
##### Sendgrid to add people to master a mailing list
def add_user_to_waiting_mailing_list(fname, lname, email):
    sg = SendGridAPIClient(os.getenv('EM_HOST_PASSWORD'))
    data = {
        "list_ids": [
            "db0c9c0c-ce0b-49c5-b73b-d622ccc3098f"
        ],
        "contacts": [
            {
                "email": email,
                "first_name":fname,
                "last_name": lname,
            }
        ]
    }

    response = sg.client.marketing.contacts.put(request_body=data)
    
def add_user_to_registered_mailing_list(fname, lname, email):
    sg = SendGridAPIClient(os.getenv('EM_HOST_PASSWORD'))
    data = {
        "list_ids": [
            "a47a488c-1ed3-444e-82c1-09d6685017f7"
        ],
        "contacts": [
            {
                "email": email,
                "first_name":fname,
                "last_name": lname,
            }
        ]
    }

    response = sg.client.marketing.contacts.put(request_body=data)

start_time = "February 17 2024, 12PM"
end_time = "February 18 2024, 3PM"
location = "TCNJ"

initial_notification_message = """We're excited to announce that registration for HackTCNJ is now open! We know you've been patiently waiting, and we appreciate your enthusiasm for our Hackathon. 

Hackathon Details:
    - Start Time: {}
    - End Time: {}
    - Location: {}

How to Register:
    1. Visit our Home Page and click the registration button: https://www.hacktcnj.com
    2. Follow the instructions to complete your registration.

Why should you attend HackTCNJ?:
    - Innovative Projects: Collaborate with like-minded individuals and bring your ideas to life.
    - Networking: Connect with industry professionals, mentors, and fellow participants.
    - Prizes: Compete for exciting prizes and gain recognition for your skills.

Don't forget to spread the word to your friends and teammates!

If you have any questions or need assistance with the registration process, feel free to reply to this email or contact our support team at contact@hacktcnj.com !
""".format(start_time, end_time, location)

reminder_notification_message = """We hope this message finds you in good spirits for the HackTCNJ! 

Hackathon Details:
    - Date: {}
    - Location: {}

How to Register:
    1. Visit our Home Page and click the registration button: https://www.hacktcnj.com
    2. Follow the instructions to complete your registration.

What to Expect:
    - Inspirational Keynotes: Kick off the hackathon with insightful talks from industry leaders.
    - Collaborative Atmosphere: Connect with fellow hackers and form teams to work on innovative projects.
    - Mentorship: Experienced mentors will be available to guide you throughout the event.
    - Prizes and Recognition: Compete for amazing prizes and showcase your skills to a wider audience.

Final Checklist:
    1. Confirm Your Registration: Double-check that you're officially registered for the event.
    2. Prepare Your Tools: Ensure your laptop and necessary tools are ready for coding and creating.
    3. Team Formation: If you haven't already, consider forming a team or finding potential collaborators.
    4. Review the Schedule: Familiarize yourself with the event schedule to make the most of your experience.

If you have any questions or need assistance with the registration process, feel free to reply to this email or contact our support team at contact@hacktcnj.com !
""".format(start_time, end_time, location)

def send_initial_notification(): 
    users = WaitingList.objects.all()
    for user in users:
        subject = "Registration Open for HackTCNJ - Register Now!"
        from_email = FROM_EMAIL
        to_email = [user.email]
        body = """Hey {},

    {}

Best,
{}
        """.format(user.full_name, initial_notification_message, TEAM_NAME)
        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=body, fail_silently=False)

def send_custom_notification(message):
    users = WaitingList.objects.all()
    for user in users:
        subject = "Reminder: HackTCNJ - Get Ready for the Hackathon Experience!"
        from_email = FROM_EMAIL
        to_email = [user.email]
        body = """Hey {},

    {}

Best,
{}
        """.format(user.full_name, message, TEAM_NAME)
        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=body, fail_silently=False)
        
def test():
    sg = SendGridAPIClient(os.getenv('EM_HOST_PASSWORD'))
    params = {'page_size': 100}
    
    response = sg.client.marketing.lists.get(
        query_params=params
    )
    
    print(response.body)