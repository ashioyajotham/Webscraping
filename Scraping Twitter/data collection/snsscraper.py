import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntwitter
import csv
import datetime

scraper = sntwitter.TwitterSearchScraper("#Maandamano")

tweets = []

for i, tweet in enumerate(scraper.get_items()):
    data = [tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount, tweet.retweetCount]
    
    tweets.append(data)

    if i > 1000:
        break

tweets_df = pd.DataFrame(tweets, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Likes', 'Retweets'])

tweets_df.head()

tweets_df.to_csv('tweets_scraper.csv', sep=',', index = False)