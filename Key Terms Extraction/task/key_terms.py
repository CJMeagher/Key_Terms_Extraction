import string
from lxml import etree
from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import namedtuple
from sklearn.feature_extraction.text import TfidfVectorizer


root = etree.parse("news.xml").getroot()


class NewsItem:
    def __init__(self, news):
        self.title = news[0].text
        self.just_the_nouns = self.__just_get_the_nouns(news[1].text.lower())

    def __just_get_the_nouns(self, text):
        lemmatizer = WordNetLemmatizer()

        def its_a_noun(word):
            lword = lemmatizer.lemmatize(word)
            if lword not in string.punctuation and lword not in stopwords.words(
                "english"
            ):
                tword = pos_tag([lword])
                if tword[0][1] == "NN":
                    return tword[0][0]
                return False

        return " ".join(
            (a_noun for word in word_tokenize(text) if (a_noun := its_a_noun(word)))
        )


news_items = [NewsItem(news) for news in root[0]]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([item.just_the_nouns for item in news_items])

WordScore = namedtuple("WordScore", "score string")
for i, vector in enumerate(vectors.toarray()):
    sorted_words = sorted(
        [
            WordScore(vector[v], k)
            for k, v in vectorizer.vocabulary_.items()
            if vector[v] > 0
        ],
        reverse=True,
    )
    print(f"{news_items[i].title}:")
    print(" ".join(word_score.string for word_score in sorted_words[:5]))
    print()
