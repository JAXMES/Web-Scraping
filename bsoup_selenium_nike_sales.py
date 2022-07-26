# pip install webdriver-manager
# pip install urllib3
# Admin permissions are needed in windows

from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


s=Service(ChromeDriverManager().install())

# Starts the browser
driver = webdriver.Chrome(service=s)

driver.get("https://www.nike.com/w/back-to-fall-4n8am")


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

product_card = soup.find_all('div', class_= 'product-card__body')
len(product_card)

# Dataframe

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Subtitle':[''], 'Price':[''], 'Sale Price':['']})


for product in product_card:
    try:
        link = product.find('a', class_= 'product-card__link-overlay').get('href')
        name = product.find('div', class_= 'product-card__title').text
        subtitle = product.find('div', class_= 'product-card__subtitle').text
        full_price = product.find('div', class_= 'product-price is--striked-out css-0').text
        sale_price = product.find('div', class_= 'product-price is--current-price css-1ydfahe').text
        df = df.append({'Link':link, 'Name':name, 'Subtitle':subtitle, 'Price':full_price, 'Sale Price':sale_price}, ignore_index = True)
        
    except:
        pass


