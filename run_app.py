__author__ = 'amit'
from tw_read_write import Twitter
from twe_bot import TweeBot

action = raw_input("What do you want to do? read/tweet: ")

if action == "read":
    screen_name = raw_input("ip screen_name: ")
    no_tweets = int(raw_input("number of tweets required: "))
    t = Twitter(screen_name)
    tweets = t.get_tweets(no_tweets)
    for tweet in tweets:
        print tweet["text"]

elif action == "tweet":
    mode = raw_input("Do you want to tweet from the file? Y/n ")
    dexter = TweeBot()
    if mode == "Y":
        read_from = raw_input("ip file path: ")
        print dexter.tweet(mode="file", file=read_from)
    elif mode == "n":
        tweet = raw_input("tweet: ")
        print dexter.tweet(tweet=tweet)
    else:
        print "wrong i/p!"