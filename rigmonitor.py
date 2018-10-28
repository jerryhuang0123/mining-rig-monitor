# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

rig_address = '0x69bb2dfdec31a13909ac3495d299979e541f0579'

def SendSms(message):
# Your Account Sid and Auth Token from twilio.com/console
	account_sid = 'twilio_account_sid'
	auth_token = 'twilio_auth_token'
	client = Client(account_sid, auth_token)

	message = client.messages \
	                .create(
	                     body=message,
	                     from_='twilio_registered_number',
	                     to='your_number'
	                 )

	print(message.sid)
	return