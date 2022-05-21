import requests
from bs4 import BeautifulSoup
import pandas as pd

# считает количество страниц у одного автора
def num_pages(link):
    soup = BeautifulSoup(requests.get(link).text, "lxml")
    pages = soup.findAll('li', class_ = 'page-item')

    for page in pages:
        if page.text == '>':
            ref = 'https://mislitel.info' + page.find('a').get('href')

    n = int(ref[len(link):].replace('?page=', ''))
    return n

# добавляет в множество все теги одного автора
def add_tags(link):
    global tags
    for i in range(1, num_pages(link) + 1):

        if i == 1:
            url = link
        else:
            url = link + '?page=' + str(i)

        soup = BeautifulSoup(requests.get(url).text, 'lxml').findAll('div', class_ = 'col-12 cont-tags')
        for s in soup:
            tags = tags.union(set(s.text.replace('#', ' ').split()))


tags = set()      
df = pd.read_csv('PsychoBot/parsing/data/links2.csv')
links = list(df['Unnamed: 1'])

for link in links:
    add_tags(link)

tags = list(tags)

df = pd.DataFrame({'' : pd.Series(tags)})
df.to_csv('python/PsychoBot/parsing/data/tags.csv')