import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from bs4 import BeautifulSoup as bs
import nltk
import requests

url = 'https://tsmliberia.com/category/fact-check/' # The URL of the website

# Get the HTML content
html = requests.get(url).text

# Parse the HTML content
soup = bs(html, 'html.parser')

# Print the parsed data of html
#print(soup.prettify())

# Get the title of the page
title = soup.title.text
print(title)

# The task is to create a dataset with fake news and real news all from the same website
# The fake news will be from the category 'fact-check'
# The real news will be from the category 'news'

# Get the links for the fake news
fake_news_links = []
for link in links:
    if 'fact-check' in link['href']:
        fake_news_links.append(link['href'])
print(fake_news_links)

# Get the links for the real news
real_news_links = []
for link in links:
    if 'news' in link['href']:
        real_news_links.append(link['href'])
print(real_news_links)

# Get the headlines for the fake news
fake_news_headlines = []
for link in fake_news_links:
    html = requests.get(link).text
    soup = bs(html, 'html.parser')
    headline = soup.title.text
    fake_news_headlines.append(headline)

# Get the headlines for the real news
real_news_headlines = []
for link in real_news_links:
    html = requests.get(link).text
    soup = bs(html, 'html.parser')
    headline = soup.title.text
    real_news_headlines.append(headline)

# Get the text for the fake news
fake_news_text = []
for link in fake_news_links:
    html = requests.get(link).text
    soup = bs(html, 'html.parser')
    text = soup.find_all('p')
    fake_news_text.append(text)

# Get the text for the real news
real_news_text = []
for link in real_news_links:
    html = requests.get(link).text
    soup = bs(html, 'html.parser')
    text = soup.find_all('p')
    real_news_text.append(text)

# Create a dataframe for the fake news
fake_news_df = pd.DataFrame({'Headline': fake_news_headlines, 'Text': fake_news_text})
print(fake_news_df)

# Create a dataframe for the real news
real_news_df = pd.DataFrame({'Headline': real_news_headlines, 'Text': real_news_text})
print(real_news_df)

# Add a column to the fake news dataframe that indicates that the news is fake
fake_news_df['Fake'] = 1
print(fake_news_df)

# Add a column to the real news dataframe that indicates that the news is real
real_news_df['Fake'] = 0
print(real_news_df)

# Combine the fake news and real news dataframes
news_df = pd.concat([fake_news_df, real_news_df])
print(news_df)