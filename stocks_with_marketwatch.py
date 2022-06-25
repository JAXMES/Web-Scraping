import requests
from bs4 import BeautifulSoup
import re

#1. Import HTML into python

url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'
page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup

#2. Price of the stock

soup.find('bg-quote', class_= 'value').text



#3. Closing price

soup.find('td', class_= 'table__cell u-semi').text


#4. 52Week range (lower, upper)

week_range_52 = soup.find_all('span', class_= 'primary')[7].text

week_range_52.split(' - ')




#5. Analyst rating

soup.find_all('li', class_= 'analyst__option active')[0].text
