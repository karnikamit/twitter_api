# -*- coding: utf-8 -*-
__author__ = "karnikamit"

import tweepy
import time
import os
from simpleconfigparser import simpleconfigparser
from elasticsearch import Elasticsearch
import json

class TweeBot:
    def __init__(self):
        self.app_route = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        configfile = simpleconfigparser()
        configfile.read(self.app_route+'/twitter_api/twitter/twitter.ini')
        self.access_token = configfile.login.access_token
        self.access_token_secret = configfile.login.access_token_secret
        self.consumer_key = configfile.login.consumer_key
        self.consumer_secret = configfile.login.consumer_secret
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)
        self.es = Elasticsearch()

    def tweet(self, tweet=None, mode="status", file=None):

        if mode == "file":
            file_open = open(file, 'r')       # Path to the file which u want to tweet.
            f = file_open.readlines()
            file_open.close()
            i = 0
            for line in f:
                line = line.encode('ascii', 'ignore')
                if i == 10:
                    break
                if not line:
                    i -= 1
                    continue

                if len(line) > 140:
                    line = line[:140]
                try:
                    self.api.update_status(status=line)
                except Exception, e:
                    print "Exception: %s" % e
                i += 1
        elif mode == "status":
            if len(tweet) > 140:
                tweet = tweet[:140]
            try:
                self.api.update_status(status=tweet)
            except Exception, e:
                print "Exception while tweeting, ", e.message

        return 'done!'

    def search(self, word, no_of_tweets):
        """

        :param word: query word
        :param no_of_tweets: int
        :return: [{screen_name: tweet}, {},...]
        """
        tweets = []
        try:
            word_search = self.api.search(q=word, lang='en', result_type='recent', count=no_of_tweets)
        except Exception, e:
            tweets.append({'Error': 'Exception: %s' % e})
        else:
            tweets = [{s.user.screen_name: s.text} for s in word_search]
            tw_body = {'search_word': word, 'tweets': json.dumps(tweets)}
            self.es.index(index='twitter', doc_type='search', body=tw_body)
        return tweets

    def get_user_details(self, user):
        u = self.api.search_users(q=user)
        details = dict()
        try:
            user_info = u[0]
            details = {'friends_count': user_info.friends_count,
                       'location': user_info.location,
                       'description': user_info.description,
                       'favourites_count': user_info.favourites_count,
                       'name': user_info.name,
                       'followers_count': user_info.followers_count}
        except Exception, e:
            details['Error'] = 'Exception: %s' % e
        return details

    def get_timeline(self, tweets):
        """

        :param tweets: number of tweets (int)
        :return: [tweets...]
        """
        return [i.text for i in self.api.home_timeline(count=tweets)]
