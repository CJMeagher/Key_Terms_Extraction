import nltk


poem = [
    "Twinkle",
    ",",
    "twinkle",
    ",",
    "little",
    "star",
    ",",
    "How",
    "I",
    "wonder",
    "what",
    "you",
    "are",
    ".",
    "Up",
    "above",
    "the",
    "world",
    "so",
    "high",
    ",",
    "Like",
    "a",
    "diamond",
    "in",
    "the",
    "sky",
    ".",
]

nouns = [tag[0] for tag in nltk.pos_tag(poem) if tag[1] == "NN"]
print("\n".join(nouns))
