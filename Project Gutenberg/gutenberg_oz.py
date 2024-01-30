import requests
from bs4 import BeautifulSoup
import nltk
import pickle
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Download the text from Project Gutenberg
url = "https://www.gutenberg.org/files/55/55-0.txt"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
text_links = soup.find_all("a", href=True)
text_url = [link["href"] for link in text_links if ".txt" in link["href"]]
print(text_url)
text = response.text

# Save the text to a file
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(response.text) # I get an error UnicodeEncodeError: 'charmap' codec can't encode characters in position 2008-2009: character maps to <undefined> so
# I changed to this: with open("text.txt", "w", encoding="utf-8") as f:
# Tokenize the text with NLTK
nltk.download("punkt")  # Download the NLTK tokenizer if needed
tokens = nltk.word_tokenize(text)

# Pickle the tokens
with open("tokens.pickle", "wb") as f:
    pickle.dump(tokens, f)

# Upload the pickle file to Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Create a new file in Google Drive
file = drive.CreateFile({"title": "tokens.pickle"})
file.SetContentFile("tokens.pickle")
file.Upload()

print("Pickle file uploaded to Google Drive.")

# SInce I aleady have a config file, we just have to link it to the Google Drive API by

# 1. Go to https://console.developers.google.com/apis/credentials
# 2. Create a new project
# 3. Click on "Create credentials" and select "OAuth client ID"
# 4. Select "Desktop app" as the application type
# 5. Click on "Download JSON" to download the config file
# 6. Rename the config file to "client_secrets.json" and place it in the same folder as this script
# 7. Run the script

# If you want to use a different config file, you can change the name in the code below
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)