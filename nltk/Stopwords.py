# Filtering using stop word
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

import nltk
from nltk.tokenize import word_tokenize,sent_tokenize

nltk.download('stopwords')
print(stopwords.words('english'))
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(s)
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
