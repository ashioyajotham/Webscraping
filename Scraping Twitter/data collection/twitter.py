import tweepy 
import json
import time
import os
import sys

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAFx1aQEAAAAAz5l1b3NRUdGdwJNiLPcwqGbEJHM%3Dj63mhEWeALUId4sKPsTNWumvhHuzo3aB1lMhNVAhEDgIznUHC0')
query = 'maandamano'

# Get tweets that contain the word maandamano

# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english 
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'entities', 
                                                'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics', 
                                     'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 
                                                'referenced_tweets', 'source', 'text', 'withheld'], max_results=100)
# Print tweets
for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)

# Print the number of tweets
print(len(tweets.data))


# Create a dictionary with the tweets
tweets_dict = {}
for tweet in tweets.data:
    tweets_dict[tweet.id] = tweet.text

# Print the dictionary
print(tweets_dict)

# Clean the dict
tweets_dict_clean = {}
for tweet in tweets_dict:
    tweets_dict_clean[tweet] = tweets_dict[tweet].replace('', ' ')

# Print the clean dict
print(tweets_dict_clean)

# Create a list with the tweets
tweets_list = []
for tweet in tweets_dict_clean:
    tweets_list.append(tweets_dict_clean[tweet])

# Print the list
print(tweets_list)

# Create a df using tweets list
tweets_df = pd.DataFrame(tweets_list, columns=['tweets'])

# Print the df
print(tweets_df)

# Save the df as a csv
tweets_df.to_csv('tweets_tw.csv', index=False)

"""
# We could increase the number of tweets by
# -increasing the number of results
# ie
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'entities',    
                                                'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics',
                                        'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics',
                                                'referenced_tweets', 'source', 'text', 'withheld'], max_results=1000)   
# -or by using the pagination
# ie
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'entities',
                                                'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics',
                                        'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics',
                                                'referenced_tweets', 'source', 'text', 'withheld'], max_results=100, next_token=tweets.meta['next_token'])

# We could also use the search_all_tweets function
# ie
tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'entities',
                                                'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics',
                                        'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics',
                                                'referenced_tweets', 'source', 'text', 'withheld'], max_results=100)

# We could also use the search_recent_tweets function
# ie
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'entities',
                                                'geo', 'id', 'in_reply_to_user_id', 'lang', 'non_public_metrics',       
                                        'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics',
                                                'referenced_tweets', 'source', 'text', 'withheld'], max_results=100)
"""