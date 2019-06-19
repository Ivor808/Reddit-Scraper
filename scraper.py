import praw
import time
from wordcloud import WordCloud
import json
import matplotlib

start_time = time.time()


def load_json_file(file):
    with open(file, 'r') as json_file:
        config_file = json.load(json_file)
    return config_file


def __get_subreddit_object(subreddit_name):
    config = load_json_file('config.json')
    reddit = praw.Reddit(client_id=config['clientId'],
                         client_secret=config['clientSecret'],
                         username=config['username'],
                         password=config['password'],
                         user_agent=config['userAgent'])
    sb = reddit.subreddit(subreddit_name)
    return sb


def word_list_to_freq_dict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))


def top_submission_to_word_cloud(subreddit_name, number_of_submissions):
    sb_submissions = __get_subreddit_object(subreddit_name).top(limit=number_of_submissions)
    top_submission = []
    for submission in sb_submissions:
        if not submission.stickied:
            top_submission.append(submission.title)
    text = " ".join([word for word in top_submission])
    wc = WordCloud()
    wc.generate(text)
    wc.to_file('test.png')


top_submission_to_word_cloud('politics', 500)

print("--- %s seconds ---" % (time.time() - start_time))
print('done')

# TODO: Maybe create the wordcloud using a stemmer algorithm
# TODO: Package the script
# TODO: Add handling of invalid subreddits
# TODO: Create wordcloud generators for HOT and maybe other types
# TODO: Create a main where user can input subreddit sort type and sort
# TODO: Add comments for each function
