import pandas as pd
from string import punctuation
from pymystem3 import Mystem
from nltk.corpus import stopwords
import gensim
import nltk


class Quote:
    user_feelings = ""
    list_for_model = []
    processed_feelings = ""

    def __init__(self):
        # files:
        # Create lemmatizer and stopwords list
        self.mystem = Mystem()
        self.russian_stopwords = stopwords.words("russian")
        # reading csv
        df = pd.read_csv('processed_q.csv', engine='python')
        # lists of quotes
        self.quote_tokens = [q.split()
                             for q in df['processed_quotes'].values.tolist()]
        self.quote_words = [q.split() for q in df['quotes'].values.tolist()]

        # model downloading

        self.model_d2v = gensim.models.doc2vec.Doc2Vec.load('models/d2v_v1-0.model')
        # suggested quotes
        self.Q_NUMBER = 10

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
            print(" ".join(self.quote_words[quote[0]]), round(quote[1], 3))


nltk.download("stopwords")
p = Quote()
print("Напечайтайте что хотите \n")
user_feelings = input()
p.preprocess_text(user_feelings)
p.basic_model()
