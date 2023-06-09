# This information has been from the 
# following website: https://world-in-paris/transport-in-france-strike-news-tips-for-traveling-to-paris/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import nltk
import warnings
warnings.filterwarnings('ignore')
import requests
from bs4 import BeautifulSoup

# We are going to scrape data from worldinparis.com about upcomingh strikes in transport
import requests
from bs4 import BeautifulSoup

url = 'https://worldinparis.com/transport-in-france-strike-news-tips-for-traveling-to-paris'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# We are going to scrape the data from the website and put it into a dataframe
# Now we can obtain the text of all the headers and paragraphs
# We will use a for loop to do this
headers = [h.get_text() for h in soup.find_all('h2')]
headers

# Obtain the text of all the paragraphs in each header
text = []
for i in range(len(headers)):
    text.append([p.get_text() for p in soup.find_all('h2')[i].find_next_siblings('p')])
text

# Create a dataframe with the headers and paragraphs
df = pd.DataFrame({'headers': headers, 'text': text})