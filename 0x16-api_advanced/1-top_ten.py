#!/usr/bin/python3
"""
This module contains one function that query the REDDIT API.
File: 1-top_ten.py
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    If an invalid subreddit is given, the function prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit10".format(subreddit)
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data['data']['children']
    for post in posts[:10]:
        print(post['data']['title'])
