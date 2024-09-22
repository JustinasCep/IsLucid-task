import os
import gensim
from gensim.utils import simple_preprocess



# open the text file as an object
doc = open('Enefit_lenktynes_tekstas.txt', encoding ='utf-8')

# preprocess the file to get a list of tokens
tokenized = []
for sentence in doc.read().split('.'):
    # the simple_preprocess function returns a list of each sentence
    tokenized.append(simple_preprocess(sentence, deacc=True))

print(tokenized)

