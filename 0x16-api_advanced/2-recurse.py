#!/usr/bin/python3
"""
Recursive function to query the Reddit API and return a list of titles of all
hot articles for a given subreddit. If no results are found or the subreddit
is invalid, returns None.

File: 2-recurse.py
"""

import requests


def recurse(subreddit, hot_list=None, after=''):
    """
    Recursively fetches the titles of all hot posts from a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    # Define the URL and headers
    base_url = 'https://www.reddit.com/r/{}/hot.json'
    params = '?limit=100&after={}'
    url = (base_url + params).format(subreddit, after)
    headers = {'User-Agent': 'python:alx-system_engineering-devops:v1.0'}

    # Make the HTTP request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is invalid
    if response.status_code != 200:
        return None

    # Load response data
    data = response.json()
    posts = data['data']['children']

    # Collect titles
    for post in posts:
        hot_list.append(post['data']['title'])

    # Check for more data
    after = data['data']['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
