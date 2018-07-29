from Preprocessing_Data import df
import math
import pickle
from collections import OrderedDict
from nltk.util import ngrams


def calculate_mutual_information(df):

    # prob_positive = 0
    # prob_negative = 0
    #
    # for item in df.polarity:
    #     if item == 1:
    #         prob_positive += 1
    #         # print(item, prob_positive)
    #     else:
    #         prob_negative += 1
    #         # print(item, prob_negative)
    #
    # prob_negative = prob_negative/len(df)
    # prob_positive = prob_positive/len(df)
    #
    # with open('pp.pickle', 'wb') as handle:
    #     pickle.dump(prob_positive, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('pp.pickle', 'rb') as handle:
    #     pp = pickle.load(handle)

    # with open('np.pickle', 'wb') as handle:
    #     pickle.dump(prob_negative, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('np.pickle', 'rb') as handle:
    #     np = pickle.load(handle)

    # print(pp)
    # print("\n")
    # print(np)
    # print("\n")
    #
    # words_prob_dict = {}
    # counter = 0
    #
    # for item in df.text:
    #     for inner_item in item:
    #
    #         if inner_item in words_prob_dict:
    #             words_prob_dict[inner_item] += 1
    #         else:
    #             words_prob_dict[inner_item] = 1
    #         counter += 1

    # print(len(words_prob_dict))
    # print(words_prob_dict)
    # print("\n")
    # print(counter)

    # with open('wpd.pickle', 'wb') as handle:
    #     pickle.dump(words_prob_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # with open('wpd.pickle', 'rb') as handle:
    #     wpd = pickle.load(handle)

    # with open('counter.pickle', 'wb') as handle:
    #     pickle.dump(counter, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # with open('counter.pickle', 'rb') as handle:
    #     counter = pickle.load(handle)

    # print(wpd)
    # print("\n")
    # # print(counter)
    #
    # counter1 = 0
    # for key in wpd:
    #
    #     wpd[key] = wpd[key]/counter
    #     counter1 += wpd[key]
    #
    # print(counter1)
    # print(len(wpd))
    # print(wpd)
    # print("\n")
    #
    # with open('wpd.pickle', 'wb') as handle:
    #     pickle.dump(wpd, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # with open('wpd.pickle', 'rb') as handle:
    #     wpd = pickle.load(handle)

    # print(wpd)
    mutual_info_dict = {}

    # pos_words_counter = 0
    # neg_words_counter = 0
    #
    # for i in range(len(df)):
    #     if df.polarity[i] == 1:
    #         for inner_i in range(len(df.text[i])):
    #             pos_words_counter += 1
    #
    #     elif df.polarity[i] == 0:
    #         for inner_i in range(len(df.text[i])):
    #             neg_words_counter += 1
    #
    # print(pos_words_counter)
    # print(neg_words_counter)
    #
    # print(len(wpd))
    counter2 = 0

    # for key in wpd:
    #     mutual_info_val = 0
    #     counter2 += 1

        # if key not in mutual_info_dict:
        #     mutual_info_dict[key] = 0

        # counter_polarity_one, counter_polarity_zero = word_polarity_counter(df, key)
        # mutual_info_val += calculate_value(pp, np, counter_polarity_one, counter_polarity_zero, pos_words_counter, neg_words_counter, wpd[key])

        # mutual_info_dict[key] = mutual_info_val
        # print(mutual_info_dict[key], key)
        # print(counter2)
        # print("\n")

    # with open('miv.pickle', 'wb') as handle:
    #     pickle.dump(mutual_info_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('miv.pickle', 'rb') as handle:
        mutual_info_dict = pickle.load(handle)

    # print(mutual_info_dict)

    mid_half_len = int(0.4*len(mutual_info_dict))
    # print(mid_half_len)

    mid = OrderedDict(sorted(mutual_info_dict.items(), key=lambda x: x[1], reverse=True)[:mid_half_len])
    
    half_unigrams_list = []
    
    for key, value in mid.items():
        half_unigrams_list.append(key)

    return half_unigrams_list


def calculate_value(prob_positive, prob_negative, counter_polarity_one, counter_polarity_zero, pos_words_counter, neg_words_counter, word_prob):
    mutual_info_value = 0
    mutual_info_value_pos = 0
    mutual_info_value_neg = 0

    if counter_polarity_zero != 0:
        mutual_info_value_neg += prob_negative*(counter_polarity_zero/neg_words_counter)*(math.log10(counter_polarity_zero/(neg_words_counter*word_prob)))
    else:
        mutual_info_value_neg = 0

    if counter_polarity_one != 0:
        mutual_info_value_pos += prob_positive*(counter_polarity_one/pos_words_counter)*(math.log10(counter_polarity_one/(pos_words_counter*word_prob)))
    else:
        mutual_info_value_pos = 0

    mutual_info_value += mutual_info_value_pos + mutual_info_value_neg

    return mutual_info_value


def word_polarity_counter(df, key):
    counter_polarity_zero = 0
    counter_polarity_one = 0

    for i in range(len(df)):
        for inner_i in df.text[i]:
            if key == inner_i and df.polarity[i] == 1:
                # print(1, inner_i)
                counter_polarity_one += 1
            elif key == inner_i and df.polarity[i] == 0:
                # print(0, inner_i)
                counter_polarity_zero += 1

    return counter_polarity_one, counter_polarity_zero


unigrams = calculate_mutual_information(df)
