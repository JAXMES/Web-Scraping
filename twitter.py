# pip install webdriver-manager
# pip install urllib3
# Admin permissions are needed in windows

from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


s=Service(ChromeDriverManager().install())

# Starts the browser
driver = webdriver.Chrome(service=s)

# Function to detect and bypass twitter phone/user authentication
def hasxpath():
    try:
        driver.find_element(By.NAME, "text")
        #driver.find_element_by_xpath(xpath)
        return True
    except:
        return False
    

driver.get("https://twitter.com/i/flow/login")
time.sleep(3)

celebrity = 'The Rock'

# name='text' is unique in HTML DOM. So there is no need to use XPath.
box_user = driver.find_element(By.NAME, "text")
type(box_user)
box_user.send_keys('mesticitre@vusra.com')
box_user.send_keys(Keys.RETURN)

time.sleep(3)

# Check if we have the authentication msg
if hasxpath() == True:
    box_auth = driver.find_element(By.NAME, "text")
    box_auth.send_keys('JamesMesticitre')
    box_auth.send_keys(Keys.RETURN)
    
    time.sleep(3)
    
    box_pass = driver.find_element(By.NAME, "password")
    box_pass.send_keys('112233445566')
    box_pass.send_keys(Keys.RETURN)
else:
    box_pass = driver.find_element(By.NAME, "password")
    box_pass.send_keys('112233445566')
    box_pass.send_keys(Keys.RETURN)
    
# Wait for serach bar (For some reason XPATH isnt working)
#WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')))
time.sleep(3)
# Twitter placeholder is more efficient since regular xpath fails
search = driver.find_element(By.XPATH, "//input[@placeholder='Search Twitter']")
search.send_keys(celebrity)
search.send_keys(Keys.RETURN)

time.sleep(3)

# Choose his profile
profile = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span')
profile.click()

time.sleep(3)

#Bsoup
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', class_= 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')

len(postings)

tweets = []

while True:
    for post in postings:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_= 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    tweets2 = list(set(tweets))
    if len(tweets2) > 100:
        break