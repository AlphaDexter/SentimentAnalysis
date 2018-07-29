from Mutual_Information import unigrams
from Preprocessing_Data import df
import pickle
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


text_file = open('stop-word-list.txt', 'r')
stop_words = text_file.read().replace(" ", "").split(",")
text_file.close()


def lexicon_classification():
    # word_scores = score_each_word(unigrams, df)
    #
    # dump_pickle_files(word_scores)
    with open('ws.pickle', 'rb') as handle:
        word_scores = pickle.load(handle)

    # print(word_scores)

    file = open('12499_10.txt', 'r')
    review_file = file.read().split(" ")
    file.close()

    for item in review_file:
        review_file[review_file.index(item)] = item.lower()

    for item in review_file:
        if item in stop_words:
            review_file[review_file.index(item)] = ''

    for item in review_file:
        ps = PorterStemmer()
        review_file[review_file.index(item)] = ps.stem(item)

    review_score = 0
    for key, value in word_scores.items():

        if key not in review_file:
            continue
        else:
            print(key)
            print(value)
            print("\n")
            review_score += value

    if review_score > 0:
        print(review_score)
        print("Positive Review")
    else:
        print(review_score)
        print("Negative Review")

    return True


def score_each_word(unigrams, df):
    word_score = {}
    check = 0

    for key in unigrams:
        print(check)
        final_score = 0
        counter = 0
        for item in df.text:
            if key in item:
                if df.iloc[counter]['polarity'] == 1:
                    final_score += 1
                else:
                    final_score -= 1
            counter += 1
        check += 1
        word_score[key] = final_score

    return word_score


def dump_pickle_files(word):
    with open('ws.pickle', 'wb') as handle:
        pickle.dump(word, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return True


lexicon_classification()
