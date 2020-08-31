import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List
from keys import consumer_key,consumer_secrets
from UserDataRetrival.commonUserInfo import *
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auth = tweepy.AppAuthHandler(consumer_key,consumer_secrets)
api = tweepy.API(auth)

def searchHastags(hastag):
    taggedTweets = []
    for tweet in tweepy.Cursor(api.search,q="#"+hastag,tweet_mode="extended",lang="en").items(100):
        taggedTweets.append(tweet.full_text)
    return taggedTweets

def getAllUserIdFromTweets(tweets):
    allUserIds = []
    for tweet in tweets:
        #print(tweet)
        ID = re.search(r'@(.*):', tweet)
        if ID is None:
            allUserIds.append(None)
            continue
        retrivedID = ID.group().split(" ")[0]
        allUserIds.append("".join(e for e in retrivedID if e.isalnum()))
    return allUserIds

def trendAnalysisByRegion(topic):
    allTaggedTweets = searchHastags(topic)
    userIds = getAllUserIdFromTweets(allTaggedTweets)
    print(userIds)
    allUsersLocation = []
    for user in userIds:
        if user is not None:
            allUsersLocation.append(get_userLocation(user))
    print(allUsersLocation)

trendAnalysisByRegion("ChadwickBoseman")
