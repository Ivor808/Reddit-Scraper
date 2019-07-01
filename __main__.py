import scraper


def main():
    sc = scraper.Scraper()
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
            sc.check_if_subreddit_exist(subreddit_name)
        except:
            print('Not a valid sub!')
            sub_fail = 1

        if sub_fail == 0:
            sc.top_submission_to_word_cloud(subreddit_name, number_of_posts_num)
        run_again = input('Would you like to run the generator again? type 1 to run again')
        if run_again == str(1):
            print('----------------------------------------')
        else:
            break


main()
