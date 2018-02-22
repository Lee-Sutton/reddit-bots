"""Provides functions for accessing the reddit api and scraping for
input keywords, minimum_score etc.
"""
import praw


def scrape_reddit(web_browser=False, limit=100, minimum_score=100,
                  keyword='fresh'):
    """
    Scrapes reddit for submissions in the hiphopheads subreddit
    either prints them to the screen or opens the links in the web
    browser.

    Args:
        web_browser (bool, optional): Opens links in web browser if true
        limit (int, optional): limit the number of links to check
        minimum_score (int, optional): Minimum submission score
    """

    reddit = praw.Reddit('hip_hop_bot')
    subreddit = reddit.subreddit("hiphopheads")

    print('Loading ...')
    line_seperator = ['-'] * 39
    line_seperator = '-'.join(line_seperator)
    for submission in subreddit.hot(limit=limit):
        if keyword.lower() in submission.title.lower() \
                and submission.score > minimum_score:
            print(line_seperator)
            print(submission.title)
            print(submission.url)
            print()
            if web_browser:
                webbrowser.open(submission.url)
