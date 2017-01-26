# Winston Bot
The goal of this project is to develop a Twitter bot which mimics the character Winston from the video game Overwatch. This project uses the python-twitter api to interact with twitter with an established
app on the site. The Winston class is where all the functionality for the various scripts are derived. As of now, two scripts are run on Linux cron jobs to process Twitter mentions every ten minutes and update
a status every week.

## Authenticating API
As mentioned above, the program uses the python-twitter API to authenticate with twitter using the proper keys provided to you through the developer apps page. In order for the Winston class to be instantiated,
you will need to have a twitter_key.py containing your correct keys to be read in. The project has a sample file where the keys must be properly set.

## Future
Future functionality includes
- Reading/Processing Tweets from @PlayOverwatch. Parse incoming updates/skins etc specifically for the character Winston
- Be more user friendly, process more Tweet mentions to be a more diverse bot
