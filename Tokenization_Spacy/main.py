import spacy

# nlp1 = spacy.blank("en")
# doc = nlp1("Dr.Ram is going to New York on a plane which cost him $500 one-way.")
# #  Each word
# list_word = []
# for each in doc:
#     list_word.append(each)
# print(list_word)


# doc2 = nlp1("Check five $")
# # Spacy showing that five is a number
# print(doc2[1])
# print(doc2[1].like_num)


# # Spacy showing that $ is a currency
# print(doc2[2])
# print(doc2[2].is_currency)

# Now, lets try with spanish language
# nlp2 = spacy.blank("es")
# text = nlp2("Hola, espero que estés bien. Gracias por visitar mi github. Dame 5 $ por favor")
# for each in text:
#     print(each, each.is_currency, each.is_digit)

# Token Customization

# from spacy.symbols import ORTH
# nlp3 = spacy.blank("en")
# nlp3.tokenizer.add_special_case("Gimme",[
#     {"ORTH":"Gim"},
#     {"ORTH":"me"}
# ])
# doc = nlp3("Gimme my money")
# print([_ for _ in doc])

# Think stats is a free book to study statistics (https://greenteapress.com/thinkstats2/thinkstats2.pdf)

# This book has references to many websites from where you can download free datasets. 
# You are an NLP engineer working for some company and you want to collect all dataset websites from this book.
# To keep exercise simple you are given a paragraph from this book and you want to grab all urls from this paragraph using spacy.
text = '''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''

nlp5 = spacy.load("en_core_web_sm")
tokens = nlp5(text)
our_urls = []
for each in tokens:
    if each.like_url:
        our_urls.append(each)
print(our_urls)

#Extract all money transaction from below sentence along with currency. Output should be,

## two $

## 500 €
transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"

line = nlp5(transactions)
for each in line:
    if each.is_currency:
        ind = each.i
        print(line[ind-1], each)





