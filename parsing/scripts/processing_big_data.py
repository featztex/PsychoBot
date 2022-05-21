import pandas as pd
import re
import pickle

# приведем столбец с тегами в порядок
def transform(str):
    l = re.sub("[\[\]\']", "", str).split(',')
    for i in range(0, len(l)):
        l[i] = l[i].strip()
    return l

df = pd.read_csv('python/PsychoBot/parsing/data/big_data.csv')
df.drop(df.columns[[0]], axis=1, inplace=True)
df = df.rename(columns={'Цитата' : 'citation', 'Автор' : 'author', 'Теги' : 'raw_tags'})

# приведем теги в человеческий вид
transform_tags = []
for i in df.raw_tags:
    transform_tags.append(transform(i))
df['tags'] = pd.Series(transform_tags)

# удалим пробелы, поменяем ё на е
df['citation'] = df['citation'].str.replace('ё','е').reset_index(drop=True)
df['citation'].str.strip().reset_index(drop=True)
df['author'] = df['author'].str.replace('ё','е').reset_index(drop=True)
df['author'].str.strip().reset_index(drop=True)

# 2 новые фичи
df['strlen'] = pd.Series([len(i) for i in df.citation])
df['num_words'] = pd.Series([len(i.split(' ')) for i in df.citation])

df.to_csv('python/PsychoBot/parsing/data/big_data.csv')