"""Command line interface to the web scraper"""
import click
from reddit_bots.scraper import scrape_reddit

@click.command()
@click.option('-k', '--keyword', default='fresh',
              help='keywords to search for')
@click.option('-m', '--minimum-score', default=100,
              help='keywords to search for')
def main(keyword, minimum_score):
    """Scrapes a subreddit for the input keyword and prints the results
    to the screen
    """
    scrape_reddit(keyword=keyword, minimum_score=minimum_score)
