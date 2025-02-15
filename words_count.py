def word_count(sentence=""):
    sentence1 = sentence.replace(".", " ").replace(',', ' ')
    words_list = sentence1.split(' ')
    words_dict = {}
    for word in words_list:
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict

print(word_count("This is the first sentence. This is the scecond sentence. This is not the fourth sentence, it is the third sentence."))