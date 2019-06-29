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
    """

    :param subreddit_name:
    :return:
    """
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


def main():
    number_of_posts_num = 50
    print("Subreddit to WordCloud Generator")
    while True:
        subreddit_name = input("What subreddit would you like a WordCloud of? (Do not include /r/): ")
        try:
            sb_submissions = __get_subreddit_object(subreddit_name).top(limit=1)
        except:
            print("Not a valid subreddit")

        number_of_posts = input("How many top posts do you want to use? Max of 1000: ")
        try:
            number_of_posts_num = int(number_of_posts)
        except ValueError:
            print("Not a valid number")

        if number_of_posts_num <= 0:
            print('Number is less than zero')
        else:
            print(type(number_of_posts_num))
            print(type(subreddit_name))
            top_submission_to_word_cloud(subreddit_name, number_of_posts_num)
            break

main()
# TODO: Maybe create the wordcloud using a stemmer algorithm
# TODO: Package the script
# TODO: Add handling of invalid subreddits
# TODO: Create wordcloud generators for HOT and maybe other types
# TODO: Create a main where user can input subreddit sort type and sort
# TODO: Add comments for each function
