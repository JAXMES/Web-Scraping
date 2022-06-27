import requests
from bs4 import BeautifulSoup


# Running website to check availability and starting BSoup
url = 'https://www.airbnb.com/s/Toronto--Ontario--Canada/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&query=Toronto%2C%20ON%2C%20Canada&place_id=ChIJpTvG15DL1IkRd8S0KlBVNTI&date_picker_type=calendar&checkin=2022-07-20&checkout=2022-07-27&adults=1&source=structured_search_input_header&search_type=user_map_move&ne_lat=43.74771847194718&ne_lng=-79.32967929299525&sw_lat=43.636731527656565&sw_lng=-79.51013714205078&zoom=10&search_by_map=true'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')

soup

#Iterating through pages from Airbnb and gathering data


while True:
    
    postings = soup.find_all('div', class_='c4mnd7m dir dir-ltr') # Get all posts in the page
    postings
    
    for post in postings:
        link = post.find('a', class_= 'ln2bl2p dir dir-ltr').get('href')
        link_full = 'https://www.airbnb.com' + link
        title = post.find('div', class_= 't1jojoys dir dir-ltr')
        title.text
        break
    
    next_page = soup.find('a', {'aria-label':'Next'}).get('href') # URL subset
    next_page
    next_page_full = 'https://www.airbnb.com'+next_page
    next_page_full

    url = next_page_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

