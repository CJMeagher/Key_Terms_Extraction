from nltk import regexp_tokenize, sent_tokenize

sentences = sent_tokenize(input())
sent_index = int(input())

print(regexp_tokenize(sentences[sent_index], "[A-z'-]+"))
