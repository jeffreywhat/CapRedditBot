import pandas as pd
import numpy as np
import nltk
import string
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
translator = str.maketrans('', '', string.punctuation)
lemmatizer = WordNetLemmatizer()


def clean_tokens(tokens):
    cleaned_tokens = []
    for token in tokens:
        token = token.lower()
        token = token.translate(translator)
        if token not in stop_words:
            if token not in "":
                token = lemmatizer.lemmatize(token)
                cleaned_tokens.append(token)
    return cleaned_tokens


