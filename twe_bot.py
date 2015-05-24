__author__ = 'karnikamit'
import tweepy
import time
import os
from simpleconfigparser import simpleconfigparser


class TweeBot:
    def __init__(self):
        self.app_route = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        configfile = simpleconfigparser()
        configfile.read(self.app_route+'/twitter_api/api_twitter.ini')
        self.access_token = configfile.login.access_token
        self.access_token_secret = configfile.login.access_token_secret
        self.consumer_key = configfile.login.consumer_key
        self.consumer_secret = configfile.login.consumer_secret
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self):
        file_open = open('', 'r')       # Path to the file which u want to tweet.
        f = file_open.readlines()
        file_open.close()
        for line in f:
            if len(line) > 140:
                line = line[:140]
            try:
                self.api.update_status(status=line)
                time.sleep(60)
            except Exception, e:
                pass
        print 'done!'


dexter = TweeBot()
dexter.tweet()
