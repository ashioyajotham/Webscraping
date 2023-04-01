import tweepy
from tweepy import OAuthHandler
import json
import os
import datetime

with open('config.json') as config_file:
    data = json.load(config_file)

# Authenticate to Twitter
access_key = data['access_key']
access_secret = data['access_secret']
consumer_key = data['consumer_key']
consumer_secret = data['consumer_secret']
bearer_token = data['bearer_token']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
print("Authenticated")

# Since it's Twitter API v2, we will use
# the bearer token to authenticate  
api = tweepy.Client(bearer_token=bearer_token)

# Get tweets that contain the word maandamano or azimio
# -is:retweet means I don't want retweets
query='maandamano OR azimio -is:retweet'

# lang:en is asking for the tweets to be in english
tweets = api.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'lang'], 
expansions=['geo.place_id'], max_results=100)

# Get place full name
for tweet in tweets.data:
    print(tweet.geo['place_id'])

# Get the date
for tweet in tweets.data:
    print(tweet.created_at)

# Get the language
for tweet in tweets.data:
    print(tweet.lang)