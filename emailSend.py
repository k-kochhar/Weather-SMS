import smtplib
from email.message import EmailMessage
import ssl
from datetime import date
import vault

def emailFormation(number, carrier):
# Formation of the receiver email
	if carrier == 'Verizon':
		return number + '@vtext.com'
	elif carrier == 'AT&T':
		return number + '@mms.att.net'
	elif carrier== 'T-Mobile':
		return number + '@tmomail.net'
	elif carrier == 'Sprint':
		return number + '@page.nextel.com'


def bodyFormation(name, city, weather, temp):
# Formation of the body message
    message = f'\nHey {name}!\nThe current weather in {city} is {weather} with a temperature of {temp:.1f}'
    return message


def emailSending(message, email):
# Retrieving sending credentials
	senderEmail = vault.senderEmail
	senderPasscode = vault.senderPasscode
	receiverEmail = email

# Depositing email content
	em = EmailMessage()
	em['From'] = senderEmail
	em['To'] = receiverEmail
	em['Subject'] = f'{date.today()}'
	em.set_content(message)

	context = ssl.create_default_context()

# Logging into and sending email through specified parameters
	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(senderEmail, senderPasscode)
		smtp.sendmail(senderEmail, receiverEmail, em.as_string())

