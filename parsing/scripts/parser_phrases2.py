import requests
from bs4 import BeautifulSoup
import pickle
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

# узнаем имя автора
def get_author_name(link):
    soup = BeautifulSoup(requests.get(link).text, "lxml")
    name = soup.find('li', class_ = 'breadcrumb-item active').find('span').text
    return name

# добавим в df инфу по одному автору
def get_author_data(link):
    global df

    name = get_author_name(link)

    for i in range(1, num_pages(link) + 1):

        if i == 1:
            url = link
        else:
            url = link + '?page=' + str(i)

        soup = BeautifulSoup(requests.get(url).text, 'lxml')

        raw_phrases = soup.findAll('div', class_ = 'col-12 cont-main')
        raw_tags = soup.findAll('div', class_ = 'col-12 cont-tags')

        if len(raw_tags) == len(raw_phrases):
            for i in range(0, len(raw_tags)):
                phrase = raw_phrases[i].text.strip()
                tags = raw_tags[i].text.replace('#', ' ').split()
                if len(phrase) <= 280:
                    row = []
                    row.append(phrase)
                    row.append(name)
                    row.append(tags)
                    df.loc[len(df.index)] = row





links = []
with open('python/PsychoBot/parsing/data/links2.pickle', 'rb') as f:
    links = pickle.load(f)

n_files = 100
for i in range(1, n_files + 1):

    col = ['Цитата', 'Автор', 'Теги']
    df = pd.DataFrame(columns=col)

    for j in range( (i - 1) * int(500 / n_files), i * int(500 / n_files)):
        get_author_data(links[j])

    df.to_csv(f'python/PsychoBot/parsing/data/data{i}.csv')