#To use the Chrome webdriver, you need to have the ChromeDriver executable installed and added to your system's PATH. You can download the appropriate version of ChromeDriver for your Chrome browser from the official website: https://sites.google.com/chromium.org/driver/
#Once you've downloaded ChromeDriver, make sure to specify the path to the executable in the webdriver.Chrome() call in the code.
#follow this tutorial - https://www.swtestacademy.com/install-chrome-driver-on-mac/

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Define the URL
url = "https://www.opentable.com/chicago-restaurants"

# Set up Selenium WebDriver (make sure to have the appropriate driver for your browser installed)
driver = webdriver.Chrome()  # You can use other browsers too

# Load the webpage using the WebDriver
driver.get(url)

# Get the page source after waiting for potential JavaScript content to load
page_source = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

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
