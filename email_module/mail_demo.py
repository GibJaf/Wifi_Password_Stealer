import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = "Cyber_Cell"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'gibviit@gmail.com'
msg.set_content('Figure out this using steghide')

files = ['hacker.jpg', 'ISACA_Pune_logo.jpeg', 'vctf_hexedit.png']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=f.name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
