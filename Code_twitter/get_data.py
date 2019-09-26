import pandas
from preprocess import preprocess

#read csv data
def get_data(csvfile,x = 0):
    data = pandas.read_csv(csvfile,sep = ',',index_col = False,header = 0)
    data.columns = ['userid','id_str','created_at','favorite_count','retweet_count','user_followers_count','post']
    data = data.drop(data.columns[[1, 2]], axis=1)
    if x != 0:
        data['punctuation'] = data['post'].map(punctuations)
        data['emoticon'],data['sarcastic'] = zip(*data['post'].map(detect_emoticon))
    data['post'] = data['post'].apply(preprocess)
    return data

data =  get_data('../twitter_data.csv')

# print data.iloc[1]['post']