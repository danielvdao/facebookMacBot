# Made by Daniel Dao #
# A facebook bot which scans everyday and sends a text for posts concerning MacBooks #
import facebook 
import time 
import os 
import sys 
import re 
from twilio.rest import TwilioRestClient 
from fbxmpp import SendMsgBot

# Get the values for global objects #

# If using heroku, use the heroku variables #
if 'DYNO' in os.environ:
	account_sid = os.environ['TWILIO_SID']
	auth_token = os.environ['TWILIO_AUTH']
	app_id = os.environ['UTBST_APPID']
	app_secret = os.environ['UTBST_APPSECRET']
	fb_token = os.environ['UTBST_FBTOKEN']
	facebook_user = os.environ['FB_USER']
	facebook_pwd = os.environ['FB_PWD']
	
# Else, use the login.properties file #
else:
	with open('login.properties', 'r') as loginFile:
		login_info = loginFile.readlines()

	facebook_user = login_info[0].replace('\n','')
	facebook_pwd = login_info[1].replace('\n','')
	account_sid = login_info[2].replace('\n','')
	auth_token = login_info[3].replace('\n','')
	app_id = login_info[4].replace('\n','')
	app_secret = login_info[5].replace('\n','')
	fb_token = login_info[6].replace('\n','')

# Get the group ID also #
group_id = "381628841954441"
graph = facebook.GraphAPI(fb_token)

# Only comment this in if extending the token #
# result = graph.extend_access_token(app_id, app_secret)
# fb_token = result['access_token']
# print fb_token

posts_query = "SELECT post_id, message, permalink, actor_id FROM stream WHERE source_id =" + group_id + " LIMIT 200"

client = TwilioRestClient(account_sid, auth_token)

# Function to pull all the posts #
def posts():
	# Getting all the comments...  #
	post_wall = graph.fql(query=posts_query)
	names = []
	item_count = 0
	messages = 'testing'
	# Get the item counts and the links for each post #
	for post in post_wall:
		msg = post['message']
		name_query = "SELECT first_name, last_name FROM user WHERE uid =" + str(post['actor_id'])
		name_query = graph.fql(query=name_query)
		
		if 'macbook' in msg.lower() and 'buying' not in msg.lower():
			# Easiest way to do this is check if price is 3 or 4, otherwise probably not selling macbook #
			match = re.search(r'\$[\d]{3,4}',msg)
			if match != None:
				item_count += 1
				name_list = name_query[0]
				temp_name_price = str(name_list['first_name']) + ' ' + str(name_list['last_name']) + ' - ' + str(match.group()) +'\n'
				names.append(temp_name_price)

	send_txt(item_count, names)
	send_msg(item_count, messages)

# Function to send the text message using twilio #
def send_txt(item_count, names):

	item_count = str(item_count)
	all_names = "".join(names)
	all_names = all_names[:-1]

	# Grammatical cases because let's be honest, english matters #

	if int(item_count) == 0:
		message = client.messages.create(to="+18322739257", from_="+18326102549", body="In the last 50 posts there were " + item_count + " Macbook posts made.")
	else:
		message = client.messages.create(to="+18322739257", from_="+18326102549", body="In the last 200 posts there were " + item_count + " Macbook posts made by:\n " + all_names)

# Function to send the facebook message to Hoai Truong #
def send_msg(item_count, messages):
	# Sender #
	jid = '623537891@chat.facebook.com'

	# Recepient #
	to = '-100000055336344@chat.facebook.com'

	xmpp = SendMsgBot(jid,to, unicode(messages))

	xmpp.credentials['api_key'] = app_id
	xmpp.credentials['access_token'] = fb_token

	if xmpp.connect(('chat.facebook.com', 5222)):
		xmpp.process(block=True)
		print 'sent'
	else:
		print 'message failed'

def main():
	posts()

main()
