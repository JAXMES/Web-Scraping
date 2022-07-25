# pip install webdriver-manager
# pip install urllib3
# Admin permissions are needed in windows

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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



#5 take screen short of the page and then get the image of the poster


