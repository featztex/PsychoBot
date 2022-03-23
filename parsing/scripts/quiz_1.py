import requests
from bs4 import BeautifulSoup
import pickle
import pandas as pd

df = pd.read_csv('python/PsychoBot/parsing/data/data_for_quiz_1.csv') 
url = 'https://allcitations.ru/tema/citaty-velikix-lyudej'
soup = BeautifulSoup(requests.get(url).text, "lxml")
sp = soup.findAll('div', class_ = 'cittext')

quotes = []
authors = []

for n in range(0, len(sp)):
    x = ''
    for i in sp[n].findAll('p'):
        x += i.text + '#'

    l = x.split('#')
    l.pop()
    if len(l) == 2:
        quotes.append(l[0])
        authors.append(l[1])

s1 = pd.Series(quotes)
s2 = pd.Series(authors)
df1 = pd.DataFrame({'Цитата' : s1, 'Автор' : s2})
df1["id"] = range(0, df1.shape[0])
df1 = df1.reindex(columns=['id','Цитата','Автор'])

df = pd.concat([df, df1], axis=0, ignore_index=True)
df = df.drop(['id'], axis = 1)
df['id'] = range(0, df.shape[0])
df = df.reindex(columns=['id','Цитата','Автор'])

for i in df.id:
    df['Цитата'][i].strip()
    df['Автор'][i].strip()

df.to_csv('python/PsychoBot/parsing/data/data_for_quiz_1.csv')