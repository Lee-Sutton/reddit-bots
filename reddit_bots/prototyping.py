import praw


def scrape_reddit():
    """
    Scrapes reddit for submissions in the hiphopheads subreddit
    either prints them to the screen or opens the links in the web
    browser.
    """

    reddit = praw.Reddit('hip_hop_bot')
    subreddit = reddit.subreddit("hiphopheads")

    print('Loading ...')
    line_seperator = ['-'] * 39
    line_seperator = '-'.join(line_seperator)
    reccomended_thread = subreddit.hot().next()
    for comment in reccomended_thread.comments:
        print(comment.body)


def main():
    """
    Parses command line args and runs the reddit bot
    """
    scrape_reddit()


if __name__ == '__main__':
    main()
