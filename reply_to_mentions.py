#! /usr/bin/python3

from winston import Winston

def main():
	winston = Winston()

	winston.verify()

	winston.get_mentions()

if __name__ == '__main__':
	main()