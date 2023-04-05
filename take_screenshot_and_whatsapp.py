# importing libraries
import pyautogui
import datetime
import subprocess, psutil
import time
import smtplib
import ssl
from email.message import EmailMessage
import os

# OPENS AN APPLICATION 
FILE = r"" # GIVE THE FILE path here
file = subprocess.Popen([FILE],shell=True) 
print(file.pid)
# os.startfile(FILE)


time.sleep(6) # Give sometime for the application to open

datetime = datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")

FILENAME = 'screenshot ' + datetime + '.jpg'

# taking screenshot from local application
screenshot = pyautogui.screenshot()
screenshot.save(FILENAME)

time.sleep(2)


# Sending Email
# PRE-REQUISITES - https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151
# Generate Application password in GMAIL. 

email_sender = ''
email_password = ''
email_receiver = ''

SUBJECT = 'Automated Email ' + datetime
BODY = """Yo !"""
ATTACHMENT = FILENAME
email_message = EmailMessage()
email_message['From'] = email_sender
email_message['To'] = email_receiver
email_message['Subject'] = SUBJECT
email_message.set_content(BODY)

# email_message.add_attachment(ATTACHMENT)
with open(ATTACHMENT, "rb") as fp:
    email_message.add_attachment(
        fp.read(), maintype="image", subtype="jpg")

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email_message.as_string())


# Closing the file
parent = psutil.Process(file.pid)
children = parent.children(recursive=True)
print(children)
child_pid = children[0].pid
print(child_pid)

subprocess.check_output("Taskkill /PID %d /F" % child_pid)