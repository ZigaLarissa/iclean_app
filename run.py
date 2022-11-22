#!/usr/bin/python3
print("iClean App")
name = input("Enter name: ")
print(f"Hello, {name} Welcome to iClean App. iClean app is an app developed by OurName that sends daily emails to users on the need to keep their environment clean.")
resp = input("Do you wish to continue?: Yes?No ")
if resp == 'Yes' or resp == 'yes' or resp == 'ye' or resp == 'y':
    print("Great! Lets get you started!")
else :
    print("Sad to see you leave")
    quit()

#Function to check user inputs valid email
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# Define a function for email validation

def check(email):
    #pass the regex and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        pass
    else :
        print("Invalid email address")
        print("Enter an email of the form johndoe@gmail.com")
        user_info()

#function to get user data
def user_info():
    global username, user_email, user_password
    username = input("Enter your username: ")
    user_email = input("Enter email: ")
    user_password = input("Enter password: ")
    check(user_email)

user_info()

#create a data structure to hold user information
user_details = {'username': username, 'user_email': user_email, 'user_password': user_password}

#EMAIL VERIFICATION

from email.message import EmailMessage
import ssl
import smtplib
import random

avcode = random.randrange(4010, 6010)

#input email of iClean app, and use the user_email inputed by user
email_sender = 'icleanapp.py@gmail.com'
email_password = 'oovufvagresdoobg'
email_receiver = user_details['user_email']

#define subject and body of the email
subject = 'Verification Code'
body = f"Hi {user_details['username']}, Your verification code is {avcode}"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

#Verify user
verification_code = int(input("Enter the verification code sent to you: "))
if avcode == verification_code:
    pass
else:
    print("Invalid Verification Code")
    quit()


#SUCCESS EMAIL

from email.message import EmailMessage
import ssl
import smtplib

#input email of iClean app, and use the user_email inputed by user
email_sender = 'icleanapp.py@gmail.com'
email_password = 'oovufvagresdoobg'
email_receiver = user_details['user_email']

#define subject and body of the email
subject = 'Hurray! Account Created'
body = """
Hi, You succesfully signed up to iClean App and your credentials have been added to the iclean database. Get Ready to receive daily emails from us on the need to keep your environment clean, tips on self and environmental hygiene.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Succesful!")
