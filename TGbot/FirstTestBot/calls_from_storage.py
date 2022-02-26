import pandas as pd
import random
from config import DATA_PATH

data = pd.read_csv(DATA_PATH)

def take_random_quote():
    rand_num = random.randint(0, data.shape[0])
    return data.iloc[rand_num]['Цитата'] + '\n' + 'Ⓒ ' + data.iloc[rand_num]['Автор'] 

