from nltk.stem import SnowballStemmer

# sent = input().split()
sent = input().split()

snowball = SnowballStemmer("german")
for w in sent:
    print(snowball.stem(w))
