#preprocessing libriaris
import nltk
nltk.download("stopwords")
#stopwords modules
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

#Create lemmatizer and stopwords list
mystem = Mystem() 
russian_stopwords = stopwords.words("russian")

#Preprocess function (stopwords, puncuation, etc)
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords\
              and token != " " \
              and token.strip() not in punctuation]
    
    text = " ".join(tokens)
    
    return text

#preprocess_text("bra По асфальту мимо цемента, Избегая зевак под аплодисменты. Обитатели спальных аррондисманов br")