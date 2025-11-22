import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

smtp_server = config["SERVER"]["smtp_server"]
port = config["SERVER"]["port"]

sender_address = config["CREDENTIALS"]["sender_address"]
sender_password = config["CREDENTIALS"]["sender_password"]
recipient_address = config["CREDENTIALS"]["recipient_address"]


def send_mail(host, content):
    msg = MIMEMultipart()
    msg["From"] = sender_address
    msg["To"] = recipient_address
    msg["Subject"] = f"{host} {content}"

    body = f"{host} {content}"
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls() 
        server.login(sender_address, sender_password)
        server.send_message(msg)

    return 
