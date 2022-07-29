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
box_job.send_keys("Data Analyst")
box_job.send_keys(Keys.RETURN)