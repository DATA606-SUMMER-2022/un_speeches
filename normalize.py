#!/usr/bin/env python3

# This is a Python script encapsulating text processing functions.

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import feature_selection

nltk.download('stopwords')
nltk.download("wordnet")
nltk.download('omw-1.4')


'''
Normalize a Text.
:parameter
    :param text: string - the text
    :param stemm: str - stemming method. None for not no stemming.
    :param lemm: str - lemmitisation method. None for no lemmatization.
    :param stopwords: list - nltk for using NLTK stop words. 
:return
    normalized text
'''
def normalize(text, stemm="porter", lemm="wordnet", stopwords="nltk"):

    ## clean (convert to lowercase and remove punctuations and characters and then strip)
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
            
    ## Tokenize (convert from string to list)
    list_words = text.split()

    ## remove Stopwords
    if stopwords == "nltk":
        list_stopwords = nltk.corpus.stopwords.words("english")
        list_words = [word for word in list_words if word not in list_stopwords]
    elif stopwords == "spacy":
        pass
    elif stopwords == "gensim":
        pass
    else:
        pass
                
    ## Stemming (remove -ing, -ly, ...)
    if stemm == "porter":
        ps = nltk.stem.porter.PorterStemmer()
        list_words = [ps.stem(word) for word in list_words]
    elif stemm == "snowball":
        ps = nltk.stem.snowball.SnowballStemmer("english")
        list_words = [ps.stem(word) for word in list_words]
    else:
        pass
                
    ## Lemmatisation (convert the word into root word)
    if lemm == "wordnet":
        lem = nltk.stem.wordnet.WordNetLemmatizer()
        list_words = [lem.lemmatize(word) for word in list_words]
    else:
        pass

    return " ".join(list_words)
