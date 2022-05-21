import requests
from bs4 import BeautifulSoup
import pickle

url_ = 'https://mislitel.info/authors'
links = []

# выберем первые 5 страниц, чтобы избежать большого числа ноунеймов в датасете
for i in range(1,6):

    if i == 1:
        url = url_
    else:
        url = url_ + '?page=' + str(i)

    data = requests.get(url)
    soup = BeautifulSoup(data.text, "lxml")
    sp = soup.findAll('td', class_ = 'razd-row')

    for i in sp:
        href = 'https://mislitel.info' + i.find('a').get('href')
        links.append(href)

with open('links2.pickle', 'wb') as f:
    pickle.dump(links, f)