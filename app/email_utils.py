from . import mail
from flask_mail import Message
from flask import current_app

def send_email(subject, recipients, body):
    msg = Message(subject, recipients=recipients, body=body)
    mail.send(msg)

