"""
Reddit WordCloud Generator: Generators wordclouds for X top posts of a specified subreddit
Created by: Ivor Zalud
6/30/2019
"""
import praw
from wordcloud import WordCloud
import json
import matplotlib


class Scraper:

    def __init__(self):
        pass

    @staticmethod
    def load_json_file(file):
        """
        Loads the JSON config file where the user inputs their reddit API info
        :param file: config file with user info
        :return: list of user info
        """
        with open(file, 'r') as json_file:
            config_file = json.load(json_file)
        return config_file

    @staticmethod
    def get_subreddit_object(subreddit_name):
        """
        Creates a subreddit object utilizing the PRAW library
        :param subreddit_name: The desired subreddit
        :return:
        """
        config = Scraper.load_json_file('config.json')
        reddit = praw.Reddit(client_id=config['clientId'],
                             client_secret=config['clientSecret'],
                             username=config['username'],
                             password=config['password'],
                             user_agent=config['userAgent'])
        sb = reddit.subreddit(subreddit_name)
        return sb

    @staticmethod
    def check_if_subreddit_exist(subreddit_name):
        """
        Checks if the given subreddit name exists
        :param subreddit_name: The subreddit to check existence of
        :return: nothing
        """
        sb = Scraper.get_subreddit_object(subreddit_name).top(limit=1)
        x = []
        for submission in sb:
            x.append(submission.title)

    @staticmethod
    def top_submission_to_word_cloud(subreddit_name, number_of_submissions):
        """
        Creates a wordcloud of the top posts from a subreddit and saves it as an image

        :param subreddit_name: The subreddit to be queried
        :param number_of_submissions: How many posts to use in generating the word cloud
        :return: No return
        """
        sb_submissions = Scraper.get_subreddit_object(subreddit_name).top(limit=number_of_submissions)
        top_submission = []
        for submission in sb_submissions:
            if not submission.stickied:
                top_submission.append(submission.title)
        text = " ".join([word for word in top_submission])
        wc = WordCloud()
        wc.generate(text)
        wc.to_file(subreddit_name + '_' + str(number_of_submissions) + '_' + 'wc.png')
