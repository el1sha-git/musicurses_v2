from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from app.core.config import EMAIL_LOGIN, EMAIL_PASSWORD


# create message object instance

async def send_message(to, message, subject):
    msg = MIMEMultipart()

    # setup the parameters of the message
    msg['From'] = EMAIL_LOGIN
    msg['To'] = to
    msg['Subject'] = subject

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server

    server = smtplib.SMTP('smtp.gmail.com: 587')
    await server.starttls()

    # Login Credentials for sending the mail
    await server.login(EMAIL_LOGIN, EMAIL_PASSWORD)

    # send the message via the server.
    await server.sendmail(EMAIL_LOGIN, to, msg.as_string())
    await server.quit()

    print("Success")
