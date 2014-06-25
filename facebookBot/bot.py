# Made by Daniel Dao #
# A facebook bot which scans everyday and sends a text for posts concerning MacBooks #
import facebook, time, os, sys 
from twilio.rest import TwilioRestClient 

# Get the values for global objects #

# If using heroku, use the heroku variables #
if 'DYNO' in os.environ:
	account_sid = os.environ['TWILIO_SID']
	auth_token = os.environ['TWILIO_AUTH']

# Else, use the login.properties file #
else:
	with open('login.properties', 'r') as loginFile:
		login_info = loginFile.readlines()

	facebook_user = login_info[0].replace('\n','')
	facebook_pwd = login_info[1].replace('\n','')
	account_sid = login_info[2].replace('\n','')
	auth_token = login_info[3].replace('\n','')

# Go to developers.facebook.com and generate an auth token #
fb_token = "CAACEdEose0cBALFgMY4ixE694ghOHAcU8OKnwjNyjixfVQfgbbRdJVB6iaxlTpBciN7qsk6FKU86lAhVoWt17BFHurQrx1Jlno4R92uJgXlQgwJ9zDxXLa08I2UDQ3lF0QjRPpokLEIJf5QBObD0CnJz6Wn6F0fpObpxbM3lxEiOigEozpfy1q5v25yVqVY5cr2RSwZDZD"

# Get the group ID also #
group_id = "381628841954441"
graph = facebook.GraphAPI(fb_token)
posts_query = "SELECT post_id, message FROM stream WHERE source_id =" + group_id + " LIMIT 50"
client = TwilioRestClient(account_sid, auth_token)


def posts():
	# Getting all the comments...  #
	post_wall = graph.fql(query=posts_query)

	for post in post_wall:
		msg = post['message']
		post_id = post['post_id']
		
		print str(msg)
		print 'Post ID: ' + post_id
		print ''
		# print str(name)


def main():
	posts()

main()
