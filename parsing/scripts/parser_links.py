import requests
from bs4 import BeautifulSoup
import pickle

url = 'http://uaforizm.com/'
data = requests.get(url)

soup = BeautifulSoup(data.text, "lxml")
sp = soup.findAll('p')

links = []

for i in sp:
    href = i.find('a').get('href')
    if ('https:' in href):
        links.append(href)

with open('links.pickle', 'wb') as f:
    pickle.dump(links, f)