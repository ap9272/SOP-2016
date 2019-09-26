import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re

#preprocessing data
def preprocess(post):

    word_remove = []
    post = re.sub("[^a-zA-Z@ ]","",post.encode('ascii', 'ignore')) #substitute non-alphabets with spaces
    post = post.lower()

    #tokenization
    post_words = post.split()

    #remove username
    for word in post_words:
        if word[0] == '@':
            word_remove.append(word)
    for word in word_remove:
        post_words.remove(word)

    #removes url
    for word in post_words:
        if "http" in word:
            post_words.remove(word)

    #word stemming
    stemmer = nltk.PorterStemmer()
    for word in post_words:
       try:
           word = stemmer.stem(word)
       except Exception as e:
           pass

    #stop word removal
    stop_words = stopwords.words('english')
    for word in post_words:
       if word in stop_words:
           post_words.remove(word)

    #removing repeated letters
    for i in range(0,len(post_words)):
        temp = ""
        count = 0
        for j in range(0,len(post_words[i])-1):
            if(post_words[i][j] == post_words[i][j+1]):
                count = count+1
            else:
                count = 0
            if(count<2):
                temp = temp+post_words[i][j]
        temp = temp+post_words[i][-1]
        post_words[i] = temp

    return post_words

#post = "@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer.  You shoulda got David Carr of Third Day to do it. ;D"

#post = preprocess(post)
#print post
