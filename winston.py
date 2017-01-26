#! /usr/bin/python3

"""
This is the Winston class. Instantiating a Winston object will give you all of the benefits of interacting with
the associated account on twitter via the built in methods. 
"""
import twitter
import json
import sys
import twitter_keys
import winston_responses

class Winston(object):
	def __init__(self):
		self.api = twitter.Api(consumer_key=twitter_keys.get_consumer_key(),
							   consumer_secret=twitter_keys.get_consumer_secret(),
							   access_token_key=twitter_keys.get_access_token_key(),
							   access_token_secret=twitter_keys.get_access_token_secret())

	def verify(self):
		try:
			self.api.VerifyCredentials()
		except twitter.error.TwitterError as error:
			sys.exit(str(error))

	def get_mentions(self):
			statuses = self.api.GetMentions()
			for status in statuses:
				json_status = json.loads(str(status))
				#print(json.dumps(json_status, separators=(',', ':'), sort_keys=True, indent=4))
				status_id = json_status['id_str']
				status_text = json_status['text']
				screenname = json_status['user']['screen_name']
				if status_id not in self.get_replied_tweets():
					self.post_mention(int(status_id), status_text, screenname)
					self.add_replied_tweet(status_id)

	def add_replied_tweet(self, tweet_id):
		with open('replied_tweets.txt', 'a') as f:
			f.write(tweet_id)
			f.write('\n')

	def get_replied_tweets(self):
		with open('replied_tweets.txt', 'r') as f:
			lines = f.read().splitlines()
			clean_lines = [l.strip('\n') for l in lines]
			return clean_lines

	def post_mention(self, status_id, status_text, screenname):
		for s in winston_responses.greetings_we_respond_to():
			if s in status_text.lower():
				message = "{} @{}".format(winston_responses.get_greeting(), screenname)
				try:
					status = self.api.PostUpdate(message)
				except UnicodeDecodeError as error:
					sys.exit(error)
				else:
					print("{} just posted: {}".format(status.user.name, status.text))
				return

	def post_tweet(self):
		message = winston_responses.get_chatter()
		try:
			status = self.api.PostUpdate(message)
		except UnicodeDecodeError as error:
			sys.exit(error)
		else:
			print("{} just posted: {}".format(status.user.name, status.text))
