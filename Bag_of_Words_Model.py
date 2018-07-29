from Mutual_Information import unigrams
from Preprocessing_Data import df
import pickle
import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

text_file = open('stop-word-list.txt', 'r')
stop_words = text_file.read().replace(" ", "").split(",")
text_file.close()

punctuation_marks_list = ['.', ',', '"', '(', ')', '<', '>', '/', '\\', '*', '&', '^', '%', '$', '#', '@', '!', '`', '~', '+', '=', '-', '_', '{', '}', '[', ']', ':', ';', "'", "?", "''", '""', '``', '--', '...']


def model(df, unigrams):

    # print(unigrams)
    # create_svm(df, unigrams)
    # print(df)

    file = open('318_10.txt', 'r')
    review_file = file.read().split(" ")
    file.close()

    review_file = preprocess_review(review_file)

    unigram_list_len = len(unigrams)
    freq_vector = [0] * unigram_list_len
    binary_vector = [0] * unigram_list_len

    for item in review_file:
        if item in unigrams:
            freq_vector[unigrams.index(item)] += 1
            binary_vector[unigrams.index(item)] = 1

    # print(freq_vector)
    # print(binary_vector)

    unigram_dict = {}
    w = 0
    b = 0
    for item in unigrams:
        unigram_dict[item] = [w, b]

    # print(unigram_dict)
    return unigram_dict


def bag_of_words(df, unigrams):
    unigram_list_len = len(unigrams)
    freq_vector = [0] * unigram_list_len
    binary_vector = [0] * unigram_list_len

    df_freq_vector = [freq_vector]*len(df)
    df_binary_vector = [binary_vector] * len(df)

    df['freq_vector'] = df_freq_vector
    df['binary_vector'] = df_binary_vector

    counter = 0

    for item in df.text:
        freq_vector = [0]*unigram_list_len
        binary_vector = [0]*unigram_list_len

        for inner_item in item:
            if inner_item in unigrams:
                freq_vector[unigrams.index(inner_item)] += 1
                binary_vector[unigrams.index(inner_item)] = 1
                # print(inner_item)

        df.set_value(counter, 'freq_vector', freq_vector)
        df.set_value(counter, 'binary_vector', binary_vector)

        print(counter)
        counter += 1

    df = df[['polarity', 'freq_vector', 'binary_vector']]

    # dump_pickle_files(df)
    # with open('df1.pickle', 'rb') as handle:
    #     df = pickle.load(handle)

    return df


def dump_pickle_files(df):
    with open('df1.pickle', 'wb') as handle:
        pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return True


def preprocess_review(review_file):

    for item in review_file:
        review_file[review_file.index(item)] = item.lower()

    for item in review_file:
        if item in stop_words:
            del review_file[review_file.index(item)]

    for item in review_file:
        if item in punctuation_marks_list:
            del review_file[review_file.index(item)]

    for item in review_file:
        ps = PorterStemmer()
        review_file[review_file.index(item)] = ps.stem(item)

    for item in review_file:
        if str(item).isdigit():
            del review_file[review_file.index(item)]

    return review_file


def train_svm(df, unigrams, unigrams_dict):

    return True


def prediction(data):
    return True


df = bag_of_words(df, unigrams)
unigrams_dict = model(df, unigrams)
train_svm(df, unigrams, unigrams_dict)
