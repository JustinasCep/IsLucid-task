import spacy
import pytextrank

nlp = spacy.load("lt_core_news_lg")
nlp.add_pipe("textrank")





with open('Enefit_lenktynes_tekstas.txt', 'r',  encoding="utf8") as file:
    doc = file.read()



text = nlp(doc)

for sent in text._.textrank.summary():
    print(sent)