# pip install webdriver-manager
# pip install urllib3
# Admin permissions are needed in windows

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


#1. Set google and type top 100 movies of all time in the box

driver.get("https://www.google.com/")

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 movies of all time')
box.send_keys(Keys.RETURN)


#2. Press enter and click on the imdb link

driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/a/h3').click()


#3. create a wait time for the page to load

time.sleep(5)


#4. scroll until the movie jaws appear

driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0,22700)')


#5 take screen short of the page and then get the image of the poster

driver.save_screenshot(r'C:\Web Scraping\whole_jaws_screenshot.png') # Entire page screenshot

driver.find_element(By.XPATH, '//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').screenshot(r'C:\Web Scraping\only_image_jaws.png')

