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

# Go to https://developers.facebook.com/tools/explorer and generate an auth token #
fb_token = "CAACEdEose0cBAIimRJJZCZC20QHxM8auAsWBM4FCF22p5sDNJJyZBVWku9eKo4ZAirZBabQaZCRtlWgKtcLYi4gSzqM9ATk3JuuOk4dU3NwJgl7x1CUEohXv5bkxPa9grQdTZBhJoAdtlPbflakb3nl5TjlSHw8NlLc0iU2FdIEe4Vr7PZAdbzzhpffAZAvHDujEPNNioZC6Y0XgZDZD"

# Get the group ID also #
group_id = "381628841954441"
graph = facebook.GraphAPI(fb_token)
posts_query = "SELECT post_id, message, permalink, actor_id FROM stream WHERE source_id =" + group_id + " LIMIT 50"

client = TwilioRestClient(account_sid, auth_token)

# Function to pull all the posts #
def posts():
	# Getting all the comments...  #
	post_wall = graph.fql(query=posts_query)
	names = []
	item_count = 0
	
	# Get the item counts and the links for each post #
	for post in post_wall:
		msg = str(post['message'])
		name_query = "SELECT first_name, last_name FROM user WHERE uid =" + str(post['actor_id'])
		name_query = graph.fql(query=name_query)
		
		if 'macbook' in msg.lower():
			name_list = name_query[0]
			temp_name = str(name_list['first_name']) + ' ' + str(name_list['last_name'])
			item_count += 1

	# send_txt(item_count, names)

# Function to send the text message using twilio #
def send_txt(item_count, names):

	item_count = str(item_count)
	message = client.messages.create(to="+18322739257", from_="+18326102549", body="in the last 100 sales there were " + item_count + " Macbook posts.")

def main():
	posts()

main()
