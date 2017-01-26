#! /usr/bin/python3

# this should be run as a chron job weekly, to post a random tweet
from winston import Winston

def main():
	winston = Winston()

	winston.verify()

	winston.post_tweet()
	
if __name__ == '__main__':
	main()