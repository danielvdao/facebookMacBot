import facebook 
from twilio.rest import TwilioRestClient 

# Get the values for global objects #

# Don't be a dumbass, set heroku variables for your auth tokens and fb account #
if 'DYNO' in os.environ:

else:
	with open('login.properties', 'r') as loginFile:
		login_info = loginFile.readLines()

	facebook_user = login_info[0].replace('\n','')
	facebook_pwd = login_info[1].replace('\n','')
	account_sid = login_info[2].replace('\n','')
	auth_token = login_info[3].replace('\n','')
client = TwilioRestClient(account_sid, auth_token)