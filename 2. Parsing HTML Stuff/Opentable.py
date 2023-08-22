#Parsing data from HTML with Requests and BeautifulSoup (NOT SELENIUM)
#also remember to have beautifulsoup4 installed
#pip install beautifulsoup4
#In this version of the code, requests is used to fetch the HTML content of the webpage, and then BeautifulSoup is used to parse the HTML and extract the data you need. This approach doesn't require the use of a web browser, unlike the selenium approach.

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://www.opentable.com/chicago-restaurants"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant information on the page (you need to inspect the page source to identify the correct tags)
restaurant_names = [name.get_text() for name in soup.find_all("span", class_="rest-row-name-text")]
restaurant_cuisines = [cuisine.get_text() for cuisine in soup.find_all("span", class_="rest-row-meta--cuisine")]
restaurant_ratings = [rating.get_text() for rating in soup.find_all("span", class_="rest-row-num-rating")]

# Create a DataFrame from the collected data
data = {
    "Restaurant Name": restaurant_names,
    "Cuisine": restaurant_cuisines,
    "Rating": restaurant_ratings
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
