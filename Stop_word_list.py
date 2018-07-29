def create_stop_word_list():
    filename_original = open('stop-word-list.txt', 'r')
    stop_word_list = filename_original.read().replace(" ", "").split(",")
    return stop_word_list


print(create_stop_word_list())
