import requests
from bs4 import BeautifulSoup
import pandas as pd

url= 'https://www.nfl.com/standings/league/2019/REG'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')

# Removes all sup tags to avoid having x z y in the team's names
for match in soup.findAll('sup'):
   match.decompose()
    
    
soup

table = soup.find('table', {'summary' : 'Standings - Detailed View'})

table

table.find_all('th')

# Iterate thourgh th and add all to a new table
headers = []

for i in table.find_all('th'):
    title = i.text
    headers.append(title)
    
# Dataframe creation + headers added
df = pd.DataFrame(columns = headers)


# Add rows to the df and grab only the first part of the first row to avoid having two names
for row in table.find_all('tr')[1:]:
    first_td = row.find_all('td')[0].find('div', class_= 'd3-o-club-fullname').text#.strip()
    data = row.find_all('td')[1:]
    row_data = [td.text for td in data]
    row_data.insert(0, first_td)
    
    length = len(df)
    df.loc[length] = row_data
    
#export
    
#df.to_csv('')