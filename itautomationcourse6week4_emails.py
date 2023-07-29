#!/usr/bin/env python3

import smtplib
import mimetypes
from email.message import EmailMessage

def generate_email(sender, recipient, subject, body, attachment_path=None):
    # Create an email message
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment_path:
        # Attach the file if provided
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as file:
            message.add_attachment(file.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=file.name)

    return message

def send_email(sender, recipient, subject, body, attachment_path=None):
    # Generate the email message
    message = generate_email(sender, recipient, subject, body, attachment_path)

    # Send the email using an SMTP server
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
