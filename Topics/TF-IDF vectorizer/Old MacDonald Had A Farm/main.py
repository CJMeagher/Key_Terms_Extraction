from sklearn.feature_extraction.text import TfidfVectorizer

file = r"data\dataset\input.txt"

vectorizer = TfidfVectorizer(
    input="file",
    use_idf=True,
    lowercase=True,
    analyzer="word",
    ngram_range=(1, 1),
    stop_words=None,
)

with open(file) as in_file:
    tfidf_matrix = vectorizer.fit_transform([in_file])

print(tfidf_matrix[0][(0, 10)])
print(tfidf_matrix[(0, 10)])
