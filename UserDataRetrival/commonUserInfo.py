import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List
from keys import consumer_key,consumer_secrets

auth = tweepy.AppAuthHandler(consumer_key,consumer_secrets)
api = tweepy.API(auth)

def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search,q=keyword,tweet_mode="extended",lang="en").items(10):
        all_tweets.append(tweet.full_text)
    print(all_tweets)
    return all_tweets

def getUserInfo(userID):
    return api.get_user(userID)

def get_TrendingList(location):
    return api.trends_place(location)

def get_followersCount(userID):
    return api.get_user(userID).followers_count

def get_followingCount(userID):
    return api.get_user(userID).friends_count

def get_userLocation(userID):
    return api.get_user(userID).location

#print(getUserInfo("Sureshpillai07"))
#print(get_TrendingList("2295424"))
#print(get_followersCount("Sureshpillai07"))