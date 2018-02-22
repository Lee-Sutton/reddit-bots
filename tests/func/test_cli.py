"""Functional unit tests for the reddit bot application"""
import signal
import subprocess
import time
from unittest.mock import patch
from click.testing import CliRunner
from reddit_bots.cli import main

DEFAULT_TIMEOUT = 2   # Seconds

def test_entry_point():
    """Checks the command line entry point of the application
    After pip installing the application the user should be able to launch
    the cli by typing reddit-bot
    """
    # The user invokes the application from the command line. They add
    # the --help flag to understand the application usage
    process = subprocess.Popen(['reddit', '--help'], stdout=subprocess.PIPE)
    output = process.stdout.read()
    assert b'Scrapes a subreddit for the input keyword' in output
    assert wait_for_process(process, DEFAULT_TIMEOUT, kill=True) == 0
    assert process.returncode == 0

@patch('reddit_bots.cli.scrape_reddit')
def test_scraping(mock_scraper):
    """When invoked the application should scrape reddit"""
    # The user invokes the application from the command line
    # supplying a subreddit they would like to scrape
    cli_runner = CliRunner()
    result = cli_runner.invoke(main, ['--keyword', 'test', '-m', 100])
    mock_scraper.assert_called_with(keyword='test', minimum_score=100)
    assert result.exit_code == 0

def wait_for_process(process, timeout, kill=False) -> int:
    """wait_for_process
    Waits for the input process to finish for the input timeout period. If
    the timeout period expires and the user has supplied the kill flag, a
    kill signal will be sent to the input process

    :param process: process to monitor
    :param timeout: timeout period to wait before returning
    :param kill: boolean indicating if the process should be killed if the
    timeout period expires
    :returns: process exit code
    """
    t_initial = time.time()
    while time.time() - t_initial < timeout:
        if process.poll() == 0:
            return process.poll()
        time.sleep(0.1)
    if kill:
        process.send_signal(signal.SIGKILL)
    return process.poll()

