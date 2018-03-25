# pull tweets from twitter api using tweepy (live)
# geomotion Twitter api app
# Joshua Cullen - Jan 2018
# tweepy docs: http://docs.tweepy.org/en/v3.5.0/index.html

import tweepy

# if unable to access, keys can be found at apps.twitter.com/app/14734411
CONSUMER_KEY = "MZmi3RBWn5i5dViJLCMGISjBi"
CONSUMER_SECRET = "l2aLIJNxk4Y4cl3CuYXreNZhOefGq9wwp5m1onUKpKRUHT0Jmi"
ACCESS_TOKEN = "257346065-4z0lgAwGcSYvs1tEra7lUEjLk01d4TUUvaKcwGeq"
ACCESS_TOKEN_SECRET = "GRvTcVEw8yWOVOK03GGR1quzrpsowkK5dyTXIXaA044hY"

# OAuth process
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# stream class to print tweets (excluding retweets)
class MyStreamListener(tweepy.StreamListener):
    """ prints tweets to terminal (excl. RTs) """
    def on_status(self, status):
        if status.text[0:4] != 'RT @':
            print('*'*80 + '\n' + status.text + '\n' + '*'*80 + '\n')

myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())

myStream.sample()            # read all tweets
#myStream.userstream()       # read user timeline (user specified during OAuth)
#myStream.filter(track=['']) # filter tweets
