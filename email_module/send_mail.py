import smtplib

import config

RECIPIENT_EMAIL = "bhavik.nahar@viit.ac.in"


def send_email(subject,msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS , config.PASSWORD)
		message = "Subject{}\n\n{}".format(subject,msg)
		server.sendmail(RECIPIENT_EMAIL , config.EMAIL_ADDRESS , message)
		server.quit()
		print("Success: Email sent !")
	except:
		print("Email failed to send.")


subject = "Test subject"
msg = "Sending you this email using python script . \n Let me know ASAP if you receive this "
send_email(subject , msg)
