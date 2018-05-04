#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for
a given subreddit or 0 if the subreddit is invalid
"""
import requests


def number_of_subscribers(subreddit):
    if type(subreddit) is not str:
        return 0
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
