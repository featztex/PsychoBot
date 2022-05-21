import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://uaforizm.com/'
data = requests.get(url)

soup = BeautifulSoup(data.text, "lxml")
sp = soup.findAll('p')

links = []

for i in sp:
    href = i.find('a').get('href')
    if ('https:' in href):
        links.append(href)

df = pd.DataFrame({'' : pd.Series(links)})
df.to_csv('python/PsychoBot/parsing/data/links.csv')