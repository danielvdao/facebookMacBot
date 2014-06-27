# Made by Daniel Dao #
# A facebook bot which scans everyday and sends a text for posts concerning MacBooks #
import facebook, time, os, sys 
from twilio.rest import TwilioRestClient 

# Get the values for global objects #

# If using heroku, use the heroku variables #
if 'DYNO' in os.environ:
	account_sid = os.environ['TWILIO_SID']
	auth_token = os.environ['TWILIO_AUTH']
	app_id = os.environ['UTBST_APPID']
	app_secret = os.environ['UTBST_APPSECRET']
# Else, use the login.properties file #
else:
	with open('login.properties', 'r') as loginFile:
		login_info = loginFile.readlines()

	facebook_user = login_info[0].replace('\n','')
	facebook_pwd = login_info[1].replace('\n','')
	account_sid = login_info[2].replace('\n','')
	auth_token = login_info[3].replace('\n','')

	if len(args) > 1:
		if args[2] == '--extend':
			app_id = login_info[4]
			app_secret = login_info[5]
# Go to https://developers.facebook.com/tools/explorer and generate an auth token #

# Attempting to extend the access token #
result = graph.extend_access_token(app_id, app_secret)
fb_token = result['access_token']
fb_token = "CAACEdEose0cBACo6sZCic9ZArG90MyWIBbZA7kM2WEsRzM7oUZACWQq4mnDYnr5Ta7hyC8qLOIEMlQ0FbvgHIgKt0PaPGxnsZB7iGUMJfWbAZBJOchVyYVKnJ1Xe7oLn4VhaIJ5D5sQvpQrV3z02UQgdP1vKoGZCH0yNWBTmYabgKSYmlD3o6RgyNg8vQBOuQsKvhPcVxp2SQZDZD"

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
		msg = post['message']
		name_query = "SELECT first_name, last_name FROM user WHERE uid =" + str(post['actor_id'])
		name_query = graph.fql(query=name_query)
		
		if 'macbook' in msg.lower():
			name_list = name_query[0]
			temp_name = str(name_list['first_name']) + ' ' + str(name_list['last_name']) + ', '
			item_count += 1
			names.append(temp_name)

	# if item_count > 2:
	# 	temp = 'and' + names[len(names) - 1]
	# 	names[len(names) - 1] = temp

	send_txt(item_count, names)

# Function to send the text message using twilio #
def send_txt(item_count, names):

	item_count = str(item_count)
	all_names = "".join(names)
	all_names = all_names[:-2]

	# Grammatical cases because let's be honest, english matters #

	if item_count < 1:
		message = client.messages.create(to="+18322739257", from_="+18326102549", body="In the last 50 posts there were " + item_count + " Macbook posts made.")
	elif item_count > 1:
		message = client.messages.create(to="+18322739257", from_="+18326102549", body="In the last 50 posts there were " + item_count + " Macbook posts made by " + all_names + ".")
	else:
		message = client.messages.create(to="+18322739257", from_="+18326102549", body="In the last 50 posts there was " + item_count + " Macbook post made by " + all_names + ".")

def main():
	posts()

main()
