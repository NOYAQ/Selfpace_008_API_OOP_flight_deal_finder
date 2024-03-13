"""
Sends a SMS with message which is passed by other.
"""
from twilio.rest import Client
import os
SID = os.environ.get("TWILIO_API_KEY")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "+447360546179"
TWILIO_VERIFIED_NUMBER = "+447432693729"

class Notification:

    def __init__(self):
        self.client = Client(SID, AUTH_TOKEN)
        
    def send_sms(self, body_message):
        message = self.client.messages.create(
            body = body_message,
            from_ = TWILIO_VIRTUAL_NUMBER,
            to = TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
