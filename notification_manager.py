import smtplib
from twilio.rest import Client

TWILIO_SID = "your twilio id"
TWILIO_AUTH_TOKEN ="your twilio token"
TWILIO_VIRTUAL_NUMBER = 'your registered num'
TWILIO_VERIFIED_NUMBER = 'your num'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.googlemail.com"
MY_EMAIL = "your mail"
MY_PASSWORD = "app pass"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP_SSL(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
