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

driver.get("https://www.indeed.com/")
time.sleep(3)

#1. Input Job Title into input box

box_job = driver.find_element(By.XPATH, "//input[@placeholder='Job title, keywords, or company']")
box_job.send_keys("painting project manager")
box_job.send_keys(Keys.RETURN)


#2. Get Link, Title, Company, Salary, Date & Location
#Bsoup
soup = BeautifulSoup(driver.page_source, 'lxml')
postings = soup.find_all('div', class_= 'job_seen_beacon')
len(postings)

df= pd.DataFrame({'Link':[''], 'Job Title':[''], 'Company':[''], 'Location':[''], 'Salary':[''], 'Date':['']})

while True:

    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_= 'job_seen_beacon')
    
    
#Loop to gather all the postings
    for post in postings:
        link = post.find('a', class_= 'jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
        link_full = 'https://www.indeed.com/'+link
        title = post.find('span').text
        company = post.find('span', class_= 'companyName').text
        try:
            location = post.find('div', class_= 'companyLocation').text.strip()
        except:
            location = 'N/A'
        # Remove extra hidden content in date
        try:
            post.find('span', class_= 'visually-hidden').decompose()
            date = post.find('span', class_= 'date').text
        except:
            date = 'N/A'
        try:
            salary = post.find('div', class_= 'attribute_snippet').text
        except:
            salary = 'N/A'
        df = df.append({'Link':link_full, 'Job Title':title, 'Company':company, 'Location':location, 'Salary':salary, 'Date':date}, 
                        ignore_index = True)
        
    try:
        button = soup.find('a', attrs = {'aria-label': 'Next'}).get('href')
        driver.get('https://www.indeed.com/'+button)
    except:
        break

