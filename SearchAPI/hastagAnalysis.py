import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List
from keys import consumer_key,consumer_secrets

auth = tweepy.AppAuthHandler(consumer_key,consumer_secrets)
api = tweepy.API(auth)


def searchHastags(hastag):
    taggedTweets = []
    for tweet in tweepy.Cursor(api.search,tweet_mode="extended", q="#"+hastag,lang="en").items(10):
        taggedTweets.append(tweet.full_text)
    return taggedTweets

print(searchHastags("ChadwickBoseman"))