# pip install webdriver-manager
# pip install urllib3
# Admin permissions are needed in windows

from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time


s=Service(ChromeDriverManager().install())

# Starts the browser
driver = webdriver.Chrome(service=s)

driver.get("https://www.nike.com/w/back-to-fall-jackets-vests-4n8amz50r7y")


# Universal code to scroll until the end
# Get the heigh of the page wait to load to compare to the new heigh and loop til we get to the end of the page

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
    
    
#Initiating BSoup
# We dont need to use request because we now have drive from selenium

soup = BeautifulSoup(driver.page_source,'lxml')


# Dataframe is not getting all the info. Lets test if we got all the lengths correct.
product_card = soup.find_all('div', class_= 'product-card__body')
len(product_card) # Correct

product_link_card = soup.find_all('a', class_= 'product-card__link-overlay')
len(product_link_card) # Correct

product_name_card = soup.find_all('div', class_= 'product-card__title')
len(product_name_card) # Correct

product_sub_card = soup.find_all('div', class_= 'product-card__subtitle')
len(product_sub_card) # Correct


product_full_price_card = soup.find_all('div', class_= 'product-price is--striked-out css-0')
len(product_full_price_card) # CULPRIT


product_sale_card = soup.find_all('div', class_= 'product-price is--current-price css-1ydfahe')
len(product_sale_card) # CULPRIT


product_lone_price_card = soup.find_all('div', class_= 'product-price is--current-price css-11s12ax')
len(product_lone_price_card) # NEW



# Dataframe

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Subtitle':[''], 'Price':[''], 'Sale Price':['']})

# loop to get all products while adding them to the df
# try - except --pass might be necessary to avoid some errors


for product in product_card:
    
    link = product.find('a', class_= 'product-card__link-overlay').get('href')
    name = product.find('div', class_= 'product-card__title').text
    subtitle = product.find('div', class_= 'product-card__subtitle').text
    #full_price = product.find('div', class_= 'product-price is--striked-out css-0').text
    #sale_price = product.find('div', class_= 'product-price is--current-price css-1ydfahe').text
        
    if product.find('div', class_= 'product-price is--striked-out css-0') is None:
        full_price = product.find('div', class_= 'product-price is--current-price css-11s12ax').text
        sale_price = 'N/A'
    else:
        full_price = product.find('div', class_= 'product-price is--striked-out css-0').text
        sale_price = product.find('div', class_= 'product-price is--current-price css-1ydfahe').text
            
        
    df = df.append({'Link':link, 'Name':name, 'Subtitle':subtitle, 'Price':full_price, 'Sale Price':sale_price}, 
                       ignore_index = True)
   


