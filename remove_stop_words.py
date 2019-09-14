import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))


def filter(words):
    processed_words = []
    for r in words:
            if not r in stop_words:
                processed_words.append(r)

    return processed_words