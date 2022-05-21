import requests
from bs4 import BeautifulSoup
import pickle
import re
import pandas as pd

# считает количество страниц внутри раздела
def num_pages(link):
    n = 1 + len(BeautifulSoup(requests.get(link).text, "lxml").findAll('a', class_ = 'post-page-numbers'))
    return n

# очистка строки от ненужных нам символов
def mysub(str):
    return re.sub(r"[\d]+ | [a-zA-Z]+", r"", a).strip()

# проверка на наличие косяков 
def check(lst1, lst2):
    if (len(lst1) == len(lst2)) and ('' not in lst1) and ('' not in lst2):
        return 1
    else:
        return 0

df = pd.read_csv('PsychoBot/parsing/data/links.csv')
links = list(df['Unnamed: 1'])

phrases = []
authors = []

for link in links:

    for i in range(1, num_pages(link) + 1):

        if i == 1:
            page_url = link
        else:
            page_url = link + '/' + str(i)

        # это отвратительная страница
        if (page_url == 'https://uaforizm.com/vyskazyvanija-zhizni.html'):
            continue
        
        page = requests.get(page_url)

        soup = BeautifulSoup(page.text, "lxml")
        
        lst1 = soup.findAll('p')[:-2]
        lst2 = soup.findAll('em')

        for i in range(0, len(lst1)):
            a = lst1[i].text
            a = mysub(a)
            lst1[i] = a
        
        for i in range(0, len(lst2)):
            a = lst2[i].text
            a = mysub(a)
            lst2[i] = a

        # удаляем имена авторов из списка lst1
        i = 0
        while i < len(lst1):
            if lst1[i] in lst2:
                del lst1[i]
            else:
                i += 1

        if check(lst1, lst2):
            phrases += lst1
            authors += lst2

# собираем датасет
ser1 = pd.Series(phrases)
ser2 = pd.Series(authors)

df = pd.DataFrame({'Цитата' : ser1, 'Автор' : ser2})
df["id"] = range(0, df.shape[0])
df = df.reindex(columns=['id','Цитата','Автор'])

df.to_csv('data.csv')