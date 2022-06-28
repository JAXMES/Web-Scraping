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

#Preparing Table
df = pd.DataFrame({'links':[''], 'Name':[''], 'Price':[''], 'Color':['']})


# Only 5 pages and put all data into a table

counter = 0
while counter < 5:
    
    # Get postings link, name, price and color of each car
    car_postings = soup.find_all('div', class_= 'l-column l-column--large-8') # Get all posts in the page
    car_postings
    
    len(car_postings)
    
    
     #TRY was added to catch any errors when we have null values. 
    #For loop gives a EOF error which does not affect the loop... Careful with While function infinite loop
    for post in car_postings:
        try:
            
            car_link = post.find('a').get('href')
            car_link_full = 'https://www.carpages.ca' + car_link
            
            car_name = post.find('a').text
            car_price = post.find('strong', class_= 'delta').text.strip()
            car_color = post.find_all('span')[-1].text.strip()
            
            df = df.append({'links':car_link_full, 'Name':car_name, 'Price':car_price, 'Color':car_color}, ignore_index = True)
            
        except:
            pass
  
    
    next_page = soup.find('a', class_= 'nextprev').get('href')# URL subset
    next_page
    next_page_full = 'https://www.carpages.ca/'+next_page
    next_page_full

    url = next_page_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    
    counter += 1