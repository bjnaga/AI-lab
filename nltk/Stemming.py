# Stemming using nltk 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

import nltk
from nltk.tokenize import word_tokenize,sent_tokenize




ps = PorterStemmer()
 
# choose some words to be stemmed
words = ["program", "programs", "programmer", "programming", "programmers"]
 
for w in words:
    print(w, " : ", ps.stem(w))
