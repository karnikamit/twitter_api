__author__ = 'karnikamit'
import tweepy
import time
import os
from simpleconfigparser import simpleconfigparser


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

    def tweet(self, tweet=None, mode="status", file=None):

        if mode == "file":
            file_open = open(file, 'r')       # Path to the file which u want to tweet.
            f = file_open.readlines()
            file_open.close()
            for line in f:
                if len(line) > 140:
                    line = line[:140]
                try:
                    self.api.update_status(status=line)
                    time.sleep(2)
                except Exception, e:
                    print "Exception", e.message
                    pass
        elif mode == "status":
            if len(tweet) > 140:
                tweet = tweet[:140]
            try:
                self.api.update_status(status=tweet)
            except Exception, e:
                print "Exception while tweeting, ", e.message

        return 'done!'

    def search(self, word):
        """

        :param word:
        :return:
        """
        tweets = []
        try:
            word_search = self.api.search(q=word, lang='en', result_type='recent', count=10, max_id='')
        except Exception, e:
            tweets.append('Exception: %s' % e)
        else:
            tweets = [{s.user.screen_name: s.text} for s in word_search]
        return tweets

if __name__ == '__main__':
    t = TweeBot()
    print t.search('mondaymotivation')
