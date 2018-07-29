from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import numpy as np
import csv
import pandas as pd
import pickle
from textblob import TextBlob


text_file = open('stop-word-list.txt', 'r')
stop_words = text_file.read().replace(" ", "").split(",")
text_file.close()

punctuation_marks_list = ['.', ',', '"', '(', ')', '<', '>', '/', '\\', '*', '&', '^', '%', '$', '#', '@', '!', '`', '~', '+', '=', '-', '_', '{', '}', '[', ']', ':', ';', "'", "?", "''", '""', '``', '--', '...']


def processing_data():
    df = pd.read_csv('C:\\Users\Ambuj\PycharmProjects\TwitterSentimentAnalysis\imdb_tr.csv', encoding='latin1')

    item_list = [0]*len(df)

    # for i in range(len(item_list)):
    #     item_list[i] = word_tokenize(df.text[i])
    #     item_list[i] = stopword_removal(item_list[i])
    #     df.text[i] = item_list[i]
    #     print(i)
    # print(df.text[i])
    # print("\n")

    # with open('sw.pickle', 'wb') as handle:
    #     pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('sw.pickle', 'rb') as handle:
    #     df = pickle.load(handle)
    #
    # for i in range(len(df)):
    #     df.text[i] = punctuation_marks_removal(df.text[i])
    #     print(i)
    #     # print(df.text[i])
    #     # print("\n")
    #
    # with open('pw.pickle', 'wb') as handle:
    #     pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('pw.pickle', 'rb') as handle:
    #     df = pickle.load(handle)
    #
    # for i in range(len(df)):
    #     df.text[i] = numeric_removal(df.text[i])
    #     print(i)
    #     # print(df.text[i])
    #     # print("\n")
    #
    # with open('nw.pickle', 'wb') as handle:
    #     pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('nw.pickle', 'rb') as handle:
    #     df = pickle.load(handle)
    #
    # for i in range(len(df)):
    #     df.text[i] = proper_noun_removal(df.text[i])
    #     print(df.text[i])
    #     print(i)
    #     print("\n")
    #
    # with open('pnr.pickle', 'wb') as handle:
    #     pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('pnr.pickle', 'rb') as handle:
    #     df = pickle.load(handle)

    # for i in range(len(df)):
    #     df.text[i] = word_stemming(df.text[i])
    #     # print(i)
    #     # print(df.text[i])
    #     # print("\n")
    #
    # with open('sfw.pickle', 'wb') as handle:
    #     pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('sfw.pickle', 'rb') as handle:
        df = pickle.load(handle)

    # print(df)

    return df


def stopword_removal(word_array):
    word_list = word_array
    filtered_words = []

    for w in word_list:
        if str(w) == "'s":
            w = 'is'
        if str(w) == "'m":
            w = 'am'
        if str(w) == "'ll":
            w = 'will'

        if w not in stop_words and str(w) != 'br':
            filtered_words.append(w)

    return filtered_words


def punctuation_marks_removal(word_array):
    pf_array = []

    for item in word_array:
        if str(item) == "n't":
            item = 'not'

        if item not in punctuation_marks_list:
            item = item.lower()
            pf_array.append(item)

    return pf_array


def numeric_removal(word_array):
    nf_array = []

    for item in range(len(word_array)):
        if str(word_array[item]).isdigit():
            continue
        else:
            nf_array.append(word_array[item])

    return nf_array


def word_stemming(word_array):
    sf_array = []
    ps = PorterStemmer()

    for item in word_array:
        sf_array.append(ps.stem(item))

    return sf_array


def proper_noun_removal(word_array):
    nr_array = []

    for key in word_array:
        blob = TextBlob(key)

        for word, tag in blob.tags:
            if tag == 'NN' or tag == 'NNS' or tag == 'NNP' or tag == 'NNPS' or tag == 'CD' or tag == 'MD':
                continue
            else:
                nr_array.append(word)

    return nr_array


df = processing_data()
