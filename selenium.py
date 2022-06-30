# pip install webdriver-manager
# pip install urllib3
# Admin permissions are needed in windows

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.get("https://www.goat.com/sneakers")

driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/a/div[1]/div[2]/div/div/span').text
