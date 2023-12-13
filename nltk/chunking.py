# chinking example 
import nltk

# https://www.nltk.org/api/nltk.tokenize.punkt.html
nltk.download('punkt') # Punkt Sentence Tokenizer

# https://www.nltk.org/api/nltk.tag.perceptron.html
nltk.download('averaged_perceptron_tagger') #  uses the perceptron algorithm to predict which POS-tag is most likely given the word.

from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize


sentence = "Educative Answers is a free web encyclopedia written by devs for devs."


# tokens = word_tokenize(sentence)
# print(tokens)

# POS tagging
# pos_tags = nltk.pos_tag(tokens)
# print(pos_tags)

chunk_patterns = r"""
    NP: {<DT>?<JJ>*<NN>}  # Chunk noun phrases
    VP: {<VB.*><NP|PP>}  # Chunk verb phrases
"""


# chunking is a powerful tool for analyzing sentences and extracting meaningful noun and verb phrases by 
# grouping words together based on their grammar

# Create a chunk parser
chunk_parser = RegexpParser(chunk_patterns)

# Perform chunking
result = chunk_parser.parse(pos_tags)

# Print the chunked result
print(result)
