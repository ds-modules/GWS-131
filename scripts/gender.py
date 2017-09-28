from nltk.corpus import names
from nltk import NaiveBayesClassifier
import random

nltk.download('names')


def extract_features(name):
    name = name.lower()
    return {
        'last_char': name[-1],
        'last_two': name[-2:],
        'last_three': name[-3:],
        'first': name[0],
        'first2': name[:1]
    }


def classify_gender(name):

    gender = classifier.classify(extract_features(name))

    if gender == "m":
        gender = "MALE"
    else:
        gender = "FEMALE"

    return gender

f_names = names.words('female.txt')
m_names = names.words('male.txt')

all_names = [(i, 'm') for i in m_names] + [(i, 'f') for i in f_names]

train_set_feat = [(extract_features(n), g) for n, g in all_names]

classifier = NaiveBayesClassifier.train(train_set_feat)
