# Scraping pages from carpages.ca - SUV

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Running website to check availability and starting BSoup
url = 'https://www.carpages.ca/used-cars/search/?category_id=6'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')

soup

while True:
    
    postings = soup.find_all('div', class_='media soft push-none rule') # Get all posts in the page
    postings