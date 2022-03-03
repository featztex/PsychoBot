import pandas as pd

df_list = []
for i in range(1, 101):
    df_list.append(pd.read_csv(f'python/PsychoBot/parsing/data/data{i}.csv'))


df = pd.concat(df_list, axis=0, ignore_index=True)
df["id"] = range(0, df.shape[0])
df = df.reindex(columns=['id','Цитата','Автор', 'Теги']) 

df.to_csv('python/PsychoBot/parsing/data/big_data.csv')