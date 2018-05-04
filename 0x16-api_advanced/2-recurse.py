#!/usr/bin/python3
"""
Querying the Reddit API recursively
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if type(subreddit) is not str:
        return None
    sub = subreddit
    api_url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(sub)
    if after is None:
        api_url += "&after={}".format(after)
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    response = response.json()
    after = response.get("data").get("after")
    hot_posts = response.get("data").get("children")
    hot_list.extend(map(lambda p: p.get("data").get("title"), hot_posts))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
