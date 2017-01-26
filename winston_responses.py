import random

def get_chatter():
	chat_list = ['Imagination is the essence of discovery.',
				 "I'm looking forward to working wth you all.",
				 "Together, we can solve any problem.",
				 "Every little bit counts.",
				 "Never accept the world as it appears to be. Dare to see it for what it could be.",
				 "'I've made a chronal accelerator, I'm sure I can do this.",
				 "Is this on?",
				 "To the former agents of #Overwatch, this is Winston! Haha ... Obviously.",
				 "We can make a difference again. The world needs us now, more than ever! Are you with me?",
				 "Enjoying the exhibit?",
				 "Alright, play time is over.",
				 "Onward and upward!",
				 "Once more into the breach.",
				 "Winston reporting.",
				 "No monkey business.",
				 "You know, they asked me to be in a movie once.",
				 "Together, we can solve any problem.",
				 "I've had some bad museum experience in the past.",
				 "This Winston came from the moon!",
				 "There's always room for self improvement.",
				 "I'm getting the hang of this.",
				 "Has anyone seen my glasses?"
				 "Curious."]
	
	return random.choice(chat_list)

def get_greeting():
	greetings = ["Hello",
				 "Hi there",
				 "Hi"]

	return random.choice(greetings)

def greetings_we_respond_to():
	return ['hello',
			'hi there',
			'hello',
			'howdy',
			'greetings',
			'hey']
