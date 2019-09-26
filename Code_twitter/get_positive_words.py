
def get_positive_words ():
    positive_words = []
    f = open('positive_words.txt','r')
    for word in f:
        positive_words.append(word.split()[0])
    return positive_words
