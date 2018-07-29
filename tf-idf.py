from Mutual_Information import unigrams
from Preprocessing_Data import df
import math


def calculate_tf():
    tf_dict = {}

    word_list = df.text.tolist()
    list_ctr = 0

    for item in word_list:
        review_tf_list = {}
        list_ctr += 1
        for inner_item in item:

            if inner_item in review_tf_list:
                review_tf_list[inner_item] += 1
            else:
                review_tf_list[inner_item] = 1
        tf_dict[list_ctr] = review_tf_list

    for item in tf_dict:
        # print(tf_idf_dict[item])
        for inner_item in tf_dict[item]:
            # print(tf_idf_dict[item][inner_item])
            tf_dict[item][inner_item] = 1.0 + math.log10(tf_dict[item][inner_item])

        print(tf_dict[item])
        print('\n')

    return tf_dict


# tf_dict = calculate_tf()


def calculate_idf():
    idf_dict = {}
    terms_list = []

    word_list = df.text.tolist()
    counter = 0

    for item in word_list:
        counter += 1

        for inner_item in item:

            if inner_item not in idf_dict:
                idf_dict[inner_item] = 0

    key_counter = 0

    for key in idf_dict:
        counter_key = 0

        for item in df.text:

            if key in item:
                counter_key += 1
                continue

        idf_dict[key] = counter_key
        print(key)
        print(idf_dict[key])
        key_counter += 1
        # print(key_counter)

    # print(idf_dict)

    return idf_dict


idf_d = calculate_idf()


