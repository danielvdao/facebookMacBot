import facebook, time, os, sys 
from twilio.rest import TwilioRestClient 

# Get the values for global objects #

# If using heroku, use the heroku variables #
if 'DYNO' in os.environ:
	facebook_user = os.environ['FACEBOOK_USER']
	facebook_pwd = os.environ['FACEBOOK_PASSWORD']
	account_sid = os.environ['TWILIO_SID']
	auth_token = os.environ['TWILIO_AUTH']

# Else, use the login.properties file #
else:
	with open('login.properties', 'r') as loginFile:
		login_info = loginFile.readLines()

	facebook_user = login_info[0].replace('\n','')
	facebook_pwd = login_info[1].replace('\n','')
	account_sid = login_info[2].replace('\n','')
	auth_token = login_info[3].replace('\n','')

# Go to developers.facebook.com and generate an auth token #
fb_token = ""

# Get the group ID also #
group_id = "381628841954441"
graph = facebook.GraphAPI(fb_token)

client = TwilioRestClient(account_sid, auth_token)

main()

def posts():
	# Getting all the comments...  #
	post_wall = graph.fql(query=posts_query)

	for post in post_wall:
		msg = post['message']
		print str(msg)


def main():
	posts()