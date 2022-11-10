import json
import pickle
import random
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout

lematizer = WordNetLemmatizer
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', ',', ';', '<', '>', '=']

for intent in intents['intents']:
    for pattern in intents['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        documents.append((word_list, intents['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

        print(documents)



