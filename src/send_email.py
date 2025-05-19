import smtplib
from email.message import EmailMessage
import os

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv("ALERT_EMAIL_FROM")
    msg['To'] = os.getenv("ALERT_EMAIL_TO")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(os.getenv("ALERT_EMAIL_FROM"), os.getenv("ALERT_EMAIL_PASSWORD"))
            server.send_message(msg)
            print("Email alert sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")