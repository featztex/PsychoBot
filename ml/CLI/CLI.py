import pandas as pd
from string import punctuation
from pymystem3 import Mystem
from nltk.corpus import stopwords
import gensim
# import nltk
# import sys
# import argparse

class Quote:
    user_feelings = ""
    list_for_model = []
    processed_feelings = ""
    path_to_csv = ""
    path_to_model = ""

    def __init__(self, path_to_csv, path_to_model):
        self.path_to_csv = path_to_csv
        self.path_to_model = path_to_model
        # files:
        # Create lemmatizer and stopwords list
        self.mystem = Mystem()
        self.russian_stopwords = stopwords.words("russian")
        # reading csv
        # processed_q.csv
        df = pd.read_csv(path_to_csv, engine='python')
        # lists of quotes
        self.quote_tokens = [q.split()
                             for q in df['processed_quotes'].values.tolist()]
        self.quote_words = [q.split() for q in df['quotes'].values.tolist()]

        # model downloading
        # models/d2v_v1-0.model
        self.model_d2v = gensim.models.doc2vec.Doc2Vec.load(path_to_model)

        # suggested quotes
        self.Q_NUMBER = 1

    # Preprocess function (stopwords, puncuation, etc)

    def preprocess_text(self, text):
        tokens = self.mystem.lemmatize(text.lower())
        tokens = [token for token in tokens if token not in self.russian_stopwords
                  and token != " "
                  and token.strip() not in punctuation]
        self.processed_feelings = " ".join(tokens)
        self.list_for_model = self.processed_feelings.split()

    def basic_model(self):
        sim = self.model_d2v.dv.most_similar(
            self.model_d2v.infer_vector(self.list_for_model), topn=self.Q_NUMBER)
        for quote in sim:
            print(" ".join(self.quote_words[quote[0]]))

#
# def createParser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('text', nargs=1)
#     return parser
#
# parser = createParser()
# namespace = parser.parse_args (sys.argv[1:])
#
# # Эту строчку можно закомментить после первого запуска
# nltk.download("stopwords")
# # при инициализации нужно указывать сначала путь к csv, потом к моделям, насколько я понял нужен полный путь
# # через относительный не смог найти как это сделать. Можно в теории использовать pathlib, но пока хз насколько имеет смысл это делать
#
# p = Quote("/home/alex/4sem/Project/PsychoBot/ml/CLI/processed_q.csv", "/home/alex/4sem/Project/PsychoBot/ml/CLI/models/d2v_v1-0.model")
# p.preprocess_text("".join(namespace.text))
# p.basic_model()
# p.basic_model()
