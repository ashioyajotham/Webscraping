# The task at hand is to scrape real estate data from a Bangladesh real estate website
# The website is: https://propertyconnectbd.com/
# The data to be scraped is:
# 1. Name of the property
# 2. Location of the property
# 3. Price of the property
# 4. Number of bedrooms
# 5. Number of bathrooms
# 6. Number of floors
# 7. Area of the property
# 8. Description of the property

# Importing the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Defining the URL
url = "https://propertyconnectbd.com/"

# Defining the headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

# Defining the function to get the HTML content
def get_html(url):
    r = requests.get(url, headers=headers)
    return r.text

# Defining the function to get the data
def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    all_products = soup.find("div", class_="row").find_all("div", class_="col-lg-4 col-md-6 col-sm-12")
    products = []
    for product in all_products:
        name = product.find("div", class_="product-content").find("h3").text.strip()
        location = product.find("div", class_="product-content").find("p").text.strip()
        price = product.find("div", class_="product-content").find("span").text.strip()
        details = product.find("div", class_="product-content").find("ul").find_all("li")
        bedrooms = details[0].text.strip()
        bathrooms = details[1].text.strip()
        floors = details[2].text.strip()
        area = details[3].text.strip()
        description = product.find("div", class_="product-content").find("p", class_="description").text.strip()
        products.append({
            "name": name,
            "location": location,
            "price": price,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "floors": floors,
            "area": area,
            "description": description
        })
    return products

# Defining the function to save the data
def save_data(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

# Defining the main function
def main():
    html = get_html(url)
    data = get_data(html)
    save_data(data, "data.csv")

# Calling the main function
if __name__ == "__main__":
    main()

# We get the user-agent by
# 1. Opening the website in the browser
# 2. Right-clicking on the page
# 3. Clicking on "Inspect"
# 4. Clicking on "Network"
# 5. Refreshing the page
# 6. Clicking on the first item in the list
# 7. Clicking on "Request Headers"
# 8. Copying the value of "User-Agent"