import pandas as pd
import random

DATA_PATH = '/home/spitsyn/PsychoBot/parsing/data/data.csv'

data = pd.read_csv(DATA_PATH)

def take_random_quote():
    rand_num = random.randint(0, data.shape[0])
    return data.iloc[rand_num]['Цитата'] + '\n' + 'Ⓒ ' + data.iloc[rand_num]['Автор'] 

