import json
import smtplib
from flask import Flask

with open('/etc/configmas.json') as config_file:
    config = json.load(config_file)

app=Flask(__name__)


@app.route("/sendMmail")
def sendMail(SUBJECT, email, TEXT):
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    sender = config['EMAIL_USER_2']
    password = config['EMAIL_PASSWORD_2']
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, email, message) # FROM, TO, MESSAGE

