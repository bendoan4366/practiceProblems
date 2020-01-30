from email.mime.text import MIMEText
import smtplib

def send_email(email_address, height):
    from_email = "ben.doan4366@gmail.com"
    #from_password =

    to_email = email_address

    subject = "Height Data"
    message = "Yo your height is %s." % height

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


    