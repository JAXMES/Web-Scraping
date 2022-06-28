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

#df = pd.DataFrame({'links':[''], 'Title':[''], 'Details':[''], 'Price':[''], 'Rating':['']})

# Get postings link, name, price and color of each car
# Only 10 pages and put all data into a table

while True:
    
    car_postings = soup.find_all('div', class_= 'l-column l-column--large-8') # Get all posts in the page
    car_postings
    
    
     #TRY was added to catch any errors when we have null values. 
    #For loop gives a EOF error which does not affect the loop... Do not run while True until complete and run the next pages code too
    for post in car_postings:
        try:
            car_link = post.find('a').get('href')
            car_link_full = 'https://www.carpages.ca' + car_link
            
            car_name = post.find('a').text
            car_price = post.find('strong', class_= 'delta').text.strip()
            car_color = post.find_all('span')[-1].text.strip()
            car_color
            
            
            break
            #df = df.append({'links':link_full, 'Title':title, 'Details':details, 'Price':price, 'Rating':rating}, ignore_index = True)
        except:
            pass
      
    
    
    next_page = soup.find('a', class_= 'nextprev').get('href') # URL subset
    next_page
    next_page_full = 'https://www.carpages.ca/'+next_page
    next_page_full

    url = next_page_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
