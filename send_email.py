import smtplib
import ssl
import os

def send_email(message): # define all email operations as one function

    host = "smtp.gmail.com"
    port = 465

    username = "zigmarszigmars19@gmail.com"
    password = os.getenv("JBN@gmail_APP_PASS_01")

    receiver = "zigmarszigmars19@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password) # login as the user of the account
        server.sendmail(username, receiver, message)