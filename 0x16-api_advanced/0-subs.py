#!/usr/bin/python3
"""
This module contains one function that requests a REDDIT API.
File: 0-subs.py
"""

import requests


def number_of_subscribers(subreddit):
    """
    Requests a REDDIT API and returns returns the number of subscribers.
    If an invalid subreddit is given, the function should return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My-Custom-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
