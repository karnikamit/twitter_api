# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from twe_bot import TweeBot

action = raw_input("What do you want to do? read/tweet/search: ")
dexter = TweeBot()
if action == "read":
    screen_name = raw_input("ip screen_name: ")
    no_tweets = int(raw_input("number of tweets required: "))
    tws = dexter.get_tweets(screen_name, no_tweets)
    print tws

elif action == "tweet":
    mode = raw_input("Do you want to tweet from the file? Y/n ")
    if mode == "Y":
        read_from = raw_input("ip file path: ")
        print dexter.tweet(mode="file", file=read_from)
    elif mode == "n":
        tweet = raw_input("tweet: ")
        print dexter.tweet(tweet=tweet)
    else:
        print "wrong i/p!"

elif action == 'search':
    word = raw_input('Search for: ')
    tweets = int(raw_input('number of tweets required: '))
    print dexter.search(word, tweets)
