import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import config
import emails_list

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # TLS port
sender_email = config.sender_email
receiver_email = emails_list.reciever_email
password = config.password

# Create a multipart message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = ', '.join(receiver_email)
message['Subject'] = 'Invitation to Webinar'

# Add the message body
message.attach(MIMEText('You are most welcomed for the annaul webinar for python conferrences in UG.', 'plain'))

# Add attachment
attachment_filename = 'test_file.txt'
attachment_path = './test_file.txt'  # Replace with the actual path to the attachment

with open(attachment_path, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename= {attachment_filename}')

message.attach(part)

# Create a secure TLS connection to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Login to your Gmail account
server.login(sender_email, password)

# Send the email
server.send_message(message)

# Clean up the connection
server.quit()

#output
print('Email has been sent to: ' + ', '.join(receiver_email))