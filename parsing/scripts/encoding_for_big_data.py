import pandas as pd
import re
import pickle

# добавляем столбец с характеристической функцией tag
def add_col(tag):
    global df
    new_col = []
    cnt = 0
    for lst in df.tags:
        if tag in lst:
            cnt += 1
            new_col.append(1)
        else:
            new_col.append(0)
    # не будем добавлять те теги, которым соответсвует меньше 0.03% цитат
    if cnt >= 10:
        df[tag] = pd.Series(new_col)

tags = []
with open('python/PsychoBot/parsing/data/tags.pickle', 'rb') as f:
    tags = pickle.load(f)

df = pd.read_csv('python/PsychoBot/parsing/data/big_data.csv') 

for tag in tags:
    add_col(tag)

df.to_csv('python/PsychoBot/parsing/data/processed_data.csv')