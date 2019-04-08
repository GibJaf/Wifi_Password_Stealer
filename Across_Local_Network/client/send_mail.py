import smtplib

import config

FILE_NAME = '0x5800e3d6dc0f'
FILE_DESC = ''

def send_email(subject,msg):
	#try:
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(config.EMAIL_ADDRESS , config.PASSWORD)
	message = "Subject{}\n\n{}".format(subject,msg)
	server.sendmail(config.EMAIL_ADDRESS ,"bhavik.nahar@viit.ac.in", message)
	server.quit()
	print("Success: Email sent !")
	#except:
	print("Email failed to send.")


subject = "Test subject"

#msg = "Sending you this again . \n Let me know ASAP if you receive this "

FILE_DESC = open(FILE_NAME,'r')
msg = FILE_DESC.read(830)
FILE_DESC.close()
send_email(subject , msg)
