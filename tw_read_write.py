__author__ = 'karnikamit'
from tweepy import OAuthHandler
import requests
import base64
import os
import json
import urllib2
from elasticsearch import Elasticsearch
es = Elasticsearch()
from simpleconfigparser import simpleconfigparser




class Twitter:
    def __init__(self, screen_name):
        self.app_route = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        configfile = simpleconfigparser()
        configfile.read(self.app_route+'/twitter_api/twitter/twitter.ini')
        self.screen_name = screen_name
        self.base_url = 'https://api.twitter.com/1.1/statuses/update.json?status='
        self.access_token = configfile.login.access_token
        self.access_token_secret = configfile.login.access_token_secret
        self.consumer_key = configfile.login.consumer_key
        self.consumer_secret = configfile.login.consumer_secret
        self.b64 = base64.b64encode(urllib2.quote(self.consumer_key) + b':' + urllib2.quote(self.consumer_secret))
        self.url = 'https://api.twitter.com/1.1/statuses/'

    def get_bearer(self):
        request = urllib2.Request("https://api.twitter.com/oauth2/token")
        request.add_header('Authorization', b'Basic ' + self.b64)
        request.add_header("Content-Type", b'application/x-www-form-urlencoded;charset=UTF-8')
        request.add_data(b'grant_type=client_credentials')
        resp = urllib2.urlopen(request)
        data = json.load(resp)
        if data['token_type'] != 'bearer':
            print"Bad token_type: " + data['token_type']
        return data['access_token']

    def get_tweets(self, t_count):        # Authenticating API requests with the bearer token and getting the tweets
        request = urllib2.Request(self.url+'user_timeline.json?count='+str(t_count)+'&screen_name=' +
                                      self.screen_name)
        request.add_header('Authorization', b'Bearer ' + self.get_bearer())
        return json.load(urllib2.urlopen(request))

    def tweet(self, status):
        headers = dict()
        headers['Authorization'] = b'Bearer ' + self.get_bearer()
        headers["Content-Type"] = b'application/x-www-form-urlencoded;charset=UTF-8'
        result = requests.post(self.base_url, headers=headers, params={'status': status},
                               data=b'grant_type=client_credentials')
        return result
