def get_negative_words ():
    negative_words = []
    f = open('negative_words.txt','r')
    for word in f:
        negative_words.append(word.split()[0])
    return negative_words
