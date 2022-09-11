import pandas as pandas
import re
import requests
from bs4 import BeautifulSoup
from datetime import date

#Pull in Aaron Judge's stats source code
url = 'https://www.espn.com/mlb/player/stats/_/id/33192/aaron-judge'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

stats = soup.find('ul', attrs = {'class': 'StatBlock__Content flex list ph4 pv3 justify-between'})

homerun_li_element = stats.find_all('li')[1]

#Today's date
today = date.today()

print("Aaron Judge has", homerun_li_element.find('div', attrs = {'class': 'StatBlockInner__Value'}).get_text() + f" homeruns in his magical 2022 season as of {today}.")