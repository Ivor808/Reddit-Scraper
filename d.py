import praw, requests, csv,obo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
start_time = time.time()
reddit = praw.Reddit(client_id = 'pnJiGPj9YrSycQ',
                     client_secret = 'g8WNac9gNqW3al5nTCPVcIV9SW8',
                     username ='pyTaste',
                     password='kailua',
                     user_agent='wordCloud')


def word_list_to_freq_dict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))


def sortfreqdict(freqdict):
    sortme = [(freqdict[key], key) for key in freqdict]
    sortme.sort()
    sortme.reverse()
    return sortme


def remove_stopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]


def get_top_submissions(subreddit_name, number_of_submissions):
    sb = reddit.subreddit(subreddit_name)
    sb_submissions = sb.top(limit=number_of_submissions)
    top_words = []
    for submission in sb_submissions:
        if not submission.stickied:
            words = submission.title.split()
            top_words.extend(words)
    top_words_filtered = remove_stopwords(top_words, obo.stopwords)
    top_words_frequency_dict = word_list_to_freq_dict(top_words_filtered)
    return top_words_frequency_dict


def create_dataframe_from_dict(dictionary):
    keylist = [key for key in dictionary]
    vallist = [dictionary[key] for key in dictionary]
    df = pd.DataFrame(list(zip(keylist, vallist)), columns=['word', 'Frequency'])
    df.sort_values(by=['Frequency'], inplace=True, ascending=False)
    return df


def dataframe_to_csv(df):
    df.to_csv('data.csv')
    return None


top_submission_words_dict = get_top_submissions('leagueoflegends', 500)
df = create_dataframe_from_dict(top_submission_words_dict)
print(df)
print("--- %s seconds ---" % (time.time() - start_time))
print('done')

# df = pd.DataFrame(list(zip(keylist,vallist)), columns= ['word', 'Frequency'])
# df.sort_values(by =['Frequency'], inplace = True, ascending=False)
# #df.to_csv('data.csv')


# TO DO: graph somehow
# test
# test2
