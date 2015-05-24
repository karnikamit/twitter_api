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
        # self.screen_name = screen_name
        # self.base_url = 'https://api.twitter.com/1.1/statuses/update.json?status='
        self.access_token = configfile.login.access_token
        self.access_token_secret = configfile.login.access_token_secret
        self.consumer_key = configfile.login.consumer_key
        self.consumer_secret = configfile.login.consumer_secret
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self):
        file_open = open('', 'r')
        f = file_open.readlines()
        file_open.close()
        for line in f:
            if len(line) <= 140:
                self.api.update_status(status=line)
                time.sleep(3)
        print 'done!'


dexter = TweeBot()
dexter.tweet()
