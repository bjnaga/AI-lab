# Tokenizing using NLTK

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

import nltk
from nltk.tokenize import word_tokenize,sent_tokenize


s = '''Good muffins cost $3.88\nin New York.  Please buy me
... two of them.\n\nThanks.'''

word_tokenize(s) 
print(word_tokenize(s) )
# print(sent_tokenize(s))
