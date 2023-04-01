import tweepy 
import json
import time
import os
import sys


# Authenticate to Twitter
auth = tweepy.OAuthHandler("RSUR3WZ6AiShbAzDiPUb6Vklp", 
    "ZyGdZtGgU0mK67rYQ9xruiahERln7GqUnN7HdE2KzPgWfwfy5Z")
auth.set_access_token("1071341427043524610-M3f2WcFTBYugm23zJoIg5v4t8Obxyy", 
    "ZF7uEu0aKAJ3HyTorIX9yWytjY996TCYwbu91JCwZh0hZ")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create a tweet

#Put your Bearer Token in the parenthesis below
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAFx1aQEAAAAAz5l1b3NRUdGdwJNiLPcwqGbEJHM%3Dj63mhEWeALUId4sKPsTNWumvhHuzo3aB1lMhNVAhEDgIznUHC0')

"""
If you don't understand search queries, there is an excellent introduction to it here: 
https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md
"""

# Get tweets that contain the hashtag #petday
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english
query = '#petday -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

"""
What context_annotations are: 
https://developer.twitter.com/en/docs/twitter-api/annotations/overview
"""
for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)