# Webscraping

## References
* "Web Scraping: The Art of Collecting Data from the Web" by Ryan Mitchell
* "Web Scraping: A Practical Guide" by David C. Vergnaud
* "Web scraping and crawling are perfectly legal – as long as you don't break the terms of service" by Mike James, a legal expert explains the legal  aspects of web scraping and the differences between scraping and crawling
* General Data Protection Regulation (GDPR) and the Computer Fraud and Abuse Act (CFAA) in the United States.

# TO add files in .gitignore 
* git rm -r --cached .
* git add .
* git commit -m "fixed untracked files"

# I have a config json file in the data/collection directory which I want to be reognised by .gitignore
* git rm -r --cached data/collection/config.json
* git add .

# In the gitignore file I will
* data/collection/config.json