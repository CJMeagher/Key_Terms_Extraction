from nltk import regexp_tokenize

sentence = input()
print(regexp_tokenize(sentence, "[A-z'-]+"))
