import requests
from bs4 import BeautifulSoup

URL = "https://genius.com/tags/cars"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Create a dictionary to store the count for each car brand
car_count = {}

# Iterate through the links and count the number of times each car brand is mentioned
for link in links:
  if "car-brands" in link['href']:
    car_brand = link.text.strip()
    if car_brand in car_count:
      car_count[car_brand] += 1
    else:
      car_count[car_brand] = 1

# Find the car brand with the highest count
most_popular_car_brand = max(car_count, key=car_count.get)

print(f"The most popular car brand in Hip-Hop is {most_popular_car_brand}")
