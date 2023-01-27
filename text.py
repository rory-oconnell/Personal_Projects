from twilio.rest import Client
import random

GOOD_MORNING_QUOTES = [
    "Good morning! Have a great day!",
    "Good morning! Today is going to be a great day!",
    "Good morning! Today is a new day, make the most of it!",   
]

cellphone = "Cell_Number"
twilio_number = "Twilio_Number"
account = "Account_SID"
token = "Account_Token"
client = Client(account, token)

quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES)-1)]
client.messages.create(to=cellphone, from_=twilio_number, body=quote)

message = client.messages.create(
    to="+Cell_Number", 
    from_="+Twilio_Number",
    body="Hello from Python!")

print(message.sid)
