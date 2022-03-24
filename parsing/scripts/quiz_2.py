import pandas as pd
import pickle

df = pd.read_csv('python/PsychoBot/parsing/data/data_for_quiz_1.csv')
x = list(set(df['Автор']))

with open('python/PsychoBot/parsing/data/authors_for_quiz_1.pickle', 'wb') as f:
    pickle.dump(x, f)