# pip install webdriver-manager
# pip install urllib3
# Admin permissions are needed in windows

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
