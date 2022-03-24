import pandas as pd
from string import punctuation
from pymystem3 import Mystem
from nltk.corpus import stopwords
import gensim
# import numpy as np
# import io
#
# import nltk
# import sys
# import argparse

class Quote:
    user_feelings = ""
    list_for_model = []
    processed_feelings = ""
    path_to_csv = ""
    path_to_model = ""
    #answer = ""

    def __init__(self, path_to_csv, path_to_model):
        self.path_to_csv = path_to_csv
        self.path_to_model = path_to_model
        # files:
        # Create lemmatizer and stopwords list
        self.mystem = Mystem()
        self.russian_stopwords = stopwords.words("russian")
        # reading csv
        self.df_35k = pd.read_csv(path_to_csv, sep=',', engine='python')
        # processed_q.csv
        df = pd.read_csv('/home/alex/4sem/Project/PsychoBot/ml/processed_data/pure_q_35k.csv', engine='python')
        # lists of quotes
        self.quote_tokens = [q.split()
                             for q in df['processed_quotes'].values.tolist()]
        self.quote_words = [q.split() for q in df['quotes'].values.tolist()]

        # model downloading
        # models/d2v_v1-0.model
        self.model = gensim.models.doc2vec.Doc2Vec.load(path_to_model)

        # suggested quotes
        self.Q_NUMBER = 6

    # Preprocess function (stopwords, puncuation, etc)
    def preprocess_text(self, text):
        tokens = self.mystem.lemmatize(text.lower())
        tokens = [token for token in tokens if token not in self.russian_stopwords \
                  and token not in [" ", "\n", "…"] \
                  and all((c not in token.strip()) for c in punctuation)]
        self.processed_feelings = " ".join(tokens)
        self.list_for_model = self.processed_feelings.split()


    def basic_model(self):
        sim = self.model.dv.most_similar(self.model.infer_vector(self.list_for_model, epochs=30), topn=self.Q_NUMBER)
        answer = []
        for quote in sim:
            #print(" ".join(self.quote_words[quote[0]]))
            answer.append((" ".join(self.quote_words[quote[0]]), self.df_35k['author'][quote[0]]))
        return answer


#
# def createParser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('text', nargs=1)
#     return parser
#
# parser = createParser()
# namespace = parser.parse_args(sys.argv[1:])
#
# # Эту строчку можно закоментить после первого запуска
# #nltk.download("stopwords")
# # при инициализации нужно указывать сначала путь к csv, потом к моделям, насколько я понял нужен полный путь
# # через относительный не смог найти как это сделать. Можно в теории использовать pathlib, но пока хз насколько имеет смысл это делать
#
# p = Quote('/home/alex/4sem/Project/PsychoBot/parsing/data/big_data.csv',
#           '../models/d2v_35k_exp.model')
# p.preprocess_text("".join(namespace.text))
# print(p.basic_model())
