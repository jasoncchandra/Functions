#Parsing data from HTML with Requests and BeautifulSoup (NOT SELENIUM)
#also remember to have beautifulsoup4 installed
#pip install beautifulsoup4
#In this version of the code, requests is used to fetch the HTML content of the webpage, and then BeautifulSoup is used to parse the HTML and extract the data you need. This approach doesn't require the use of a web browser, unlike the selenium approach.

import re
import pandas as pd
from bs4 import BeautifulSoup
import requests

def parse_html(html):
    data, item = pd.DataFrame(), {}
    soup = BeautifulSoup(html, 'lxml')
    for i, resto in enumerate(soup.find_all('div', class_='rest-row-info')):
        item['name'] = resto.find('span', class_='rest-row-name-text').text

        booking = resto.find('div', class_='booking')
        item['bookings'] = re.search('\d+', booking.text).group() if booking else 'NA'

        rating = resto.find('div', class_='star-rating-score')
        item['rating'] = float(rating['aria-label'].split()[0]) if rating else 'NA'

        reviews = resto.find('span', class_='underline-hover')
        item['reviews'] = int(re.search('\d+', reviews.text).group()) if reviews else 'NA'

        item['price'] = int(resto.find('div', class_='rest-row-pricing').find('i').text.count('$'))
        item['cuisine'] = resto.find('span', class_='rest-row-meta--cuisine rest-row-meta-text sfx1388addContent').text
        item['location'] = resto.find('span', class_='rest-row-meta--location rest-row-meta-text sfx1388addContent').text
        data[i] = pd.Series(item)
    return data.T

# Use requests to get the HTML content
url = "https://www.opentable.com/new-york-restaurant-listings"
response = requests.get(url)
if response.status_code == 200:
    page_source = response.text
    new_data = parse_html(page_source)
    new_data.to_csv('results.csv', index=False)
    print("Data downloaded and parsed successfully.")
else:
    print("Failed to retrieve the page content.")

restaurants = pd.read_csv('results.csv')
print(restaurants)
