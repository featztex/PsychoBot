import requests
import pickle
from bs4 import BeautifulSoup

url = 'https://uaforizm.com/aforizmy-i-citaty-po-alfavitu.html'
data = requests.get(url)

soup = BeautifulSoup(data.text, "lxml")

themes = soup.findAll('p')
lst = []

for theme in themes:
    if ('https:' in theme.find('a').get('href')):
        lst.append(theme.find('a').text)

with open('themes.pickle', 'wb') as f:
    pickle.dump(lst, f)