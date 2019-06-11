import praw, requests, csv, obo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

reddit = praw.Reddit(client_id = 'pnJiGPj9YrSycQ',
                     client_secret = 'g8WNac9gNqW3al5nTCPVcIV9SW8',
                     username ='pyTaste',
                     password='kailua',
                     user_agent='wordCloud')

subreddit = reddit.subreddit('politics')
hot_sub = subreddit.top(limit=500)


def wordlisttofreqdict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))


def sortfreqdict(freqdict):
    sortme = [(freqdict[key], key) for key in freqdict]
    sortme.sort()
    sortme.reverse()
    return sortme


def removestopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]


hot_words = []
hot_freq = []
hot_dict = {}
for submission in hot_sub:
    if not submission.stickied:
        words = submission.title.split()
        hot_words.extend(words)
        hot_words = removestopwords(hot_words, obo.stopwords)
        hot_dict = wordlisttofreqdict(hot_words)
        keylist = [key for key in hot_dict]
        vallist = [hot_dict[key] for key in hot_dict]


print('done')

df = pd.DataFrame(list(zip(keylist,vallist)), columns= ['word', 'Frequency'])
df.sort_values(by =['Frequency'], inplace = True, ascending=False)
df.to_csv('data.csv')
# TO DO: graph somehow
# test
# test2
