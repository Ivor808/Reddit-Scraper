import praw
from wordcloud import WordCloud
import json
import matplotlib


def __load_json_file(file):
    """
    Loads the JSON config file where the user inputs their reddit API info
    :param file: config file with user info
    :return: list of user info
    """
    with open(file, 'r') as json_file:
        config_file = json.load(json_file)
    return config_file


def __get_subreddit_object(subreddit_name):
    """
    Creates a subreddit object utilizing the PRAW library
    :param subreddit_name: The desired subreddit
    :return:
    """
    config = __load_json_file('config.json')
    reddit = praw.Reddit(client_id=config['clientId'],
                         client_secret=config['clientSecret'],
                         username=config['username'],
                         password=config['password'],
                         user_agent=config['userAgent'])
    sb = reddit.subreddit(subreddit_name)
    return sb


def __check_if_subreddit_exist(subreddit_name):
    """
    Checks if the given subreddit name exists
    :param subreddit_name: The subreddit to check existence of
    :return: nothing
    """
    sb = __get_subreddit_object(subreddit_name).top(limit=1)
    x = []
    for submission in sb:
        x.append(submission.title)


def top_submission_to_word_cloud(subreddit_name, number_of_submissions):
    """
    Creates a wordcloud of the top posts from a subreddit and saves it as an image

    :param subreddit_name: The subreddit to be queried
    :param number_of_submissions: How many posts to use in generating the word cloud
    :return: No return
    """
    sb_submissions = __get_subreddit_object(subreddit_name).top(limit=number_of_submissions)
    top_submission = []
    for submission in sb_submissions:
        if not submission.stickied:
            top_submission.append(submission.title)
    text = " ".join([word for word in top_submission])
    wc = WordCloud()
    wc.generate(text)
    wc.to_file(subreddit_name + '_' + str(number_of_submissions) + '_' + 'wc.png')


def main():
    number_of_posts_num = 15
    print("Subreddit to WordCloud Generator")
    while True:
        sub_fail = 0
        subreddit_name = input("What subreddit would you like a WordCloud of? (Do not include /r/): ")

        number_of_posts = input("How many top posts do you want to use? Max of 1000: ")
        try:
            number_of_posts_num = int(number_of_posts)
        except ValueError:
            print("Not a valid number")

        if number_of_posts_num <= 0:
            print('Number is less than zero')

        try:
            __check_if_subreddit_exist(subreddit_name)
        except:
            print('Not a valid sub!')
            sub_fail = 1

        if sub_fail == 0:
            top_submission_to_word_cloud(subreddit_name, number_of_posts_num)
        run_again = input('Would you like to run the generator again? type 1 to run again')
        if run_again == str(1):
            print('----------------------------------------')
        else:
            break


main()

