import nltk


sent = [
    "The",
    "horse",
    "that",
    "was",
    "raced",
    "past",
    "the",
    "barn",
    "fell",
    "down",
    ".",
]
tag = [result for result in nltk.pos_tag(sent) if result[0] == "raced"]
print(tag[0][1])
