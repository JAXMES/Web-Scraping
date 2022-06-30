# pip install webdriver-manager
# pip install urllib3
# Admin permissions are needed in windows

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service(ChromeDriverManager().install())
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
