import facebook 
from twilio.rest import TwilioRestClient 

# Get the values for global objects #

# Don't be a dumbass, set heroku variables for your auth tokens and fb account #

account_sid = "ACeda058cd635ee4e2c9c6126740a6fdd8"
auth_token = 
client = TwilioRestClient(account_sid, auth_token)