from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "account_sid"
# Your Auth Token from twilio.com/console
auth_token  = "auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+cell", 
    from_="+twilio",
    body="Hello from Python!")

print(message.sid)
