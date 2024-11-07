import spacy
import nltk
from nltk import PorterStemmer
stemmer = PorterStemmer()
words = ["apple", "eating","plays", "ate", "giving","denied"]
for word in words:
    print(word, " | ", stemmer.stem(word))

nlp = spacy.load("en_core_web_sm")
doc = nlp("apple eating plays giving denied")
for each in doc:
    print(each, " | ", each.lemma_)
    

