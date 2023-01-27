from twilio.rest import Client
import random

GOOD_MORNING_QUOTES = [
    "Good morning! Have a great day!",
    "Good morning! Today is going to be a great day!",
    "Good morning! Today is a new day, make the most of it!",   
]

cellphone = "+353874629533"
twilio_number = "+15735153671"
account = "AC9e9e80de3a30c90481869b9b9efb23ca"
token = "f52326d27b7bd05e2f3eebcd5803a29c"
client = Client(account, token)

quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES)-1)]
client.messages.create(to=cellphone, from_=twilio_number, body=quote)

message = client.messages.create(
    to="+353874629533", 
    from_="+15735153671",
    body="Hello from Python!")

print(message.sid)