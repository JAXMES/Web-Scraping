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


driver.get("https://www.goat.com/sneakers")

#Get all postings from 1-20 in the sneakers section
for i in range(1, 20):
    price = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div/div/span').text
    print(price)
    
# Google Input

driver.get("https://www.google.com/")

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Selenium')
box.send_keys(Keys.RETURN)


# Clicking on a Button

button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
button.click()

follow_link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3').click()


# Screenshots (.save for the entire page)

driver.save_screenshot(r'C:\Web Scraping\selenium.png')

# XPATH screenshot

driver.find_element(By.XPATH, '/html/body/div/main/div[4]/div[5]/a/img').screenshot(r'C:\Web Scraping\selenium1.png')




# Search & screenshot the selected picture of a long haired gray cat

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('long haired gray cat')
box.send_keys(Keys.RETURN)

driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click() # Go to images

# we might need the full XPATH
#driver.find_element(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[2]/a[1]/div[1]/img').screenshot(r'C:\Web Scraping\cats.png')



# Self-Scrolling

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('long haired gray cat')
box.send_keys(Keys.RETURN)

driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click() # Go to images

driver.execute_script('return document.body.scrollHeight') # Height of the page

driver.execute_script('window.scrollTo(0,5000)') # Scroll until the specified height of the page

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') # Keep scrolling down



# Wait Times

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Cat')
box.send_keys(Keys.RETURN)

# use this to wait for specific elements to load
#element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, '')))

# OR use this to wait a few seconds
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a').click()




