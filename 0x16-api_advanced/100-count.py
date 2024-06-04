#!/usr/bin/python3
"""
Count keyword occurrences in subreddit post titles recursively.
File: 100-count.py
"""
import re
import requests


def count_words(subreddit, word_list, after='', count_dict=None):
    """
    A recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords.
    """
    if count_dict is None:
        count_dict = {}
        word_list = [word.lower() for word in word_list]

    api_url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
            subreddit, after)
    headers = {"User-Agent": "Custom-User-Agent"}
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            count = len(re.findall(r'\b{}\b'.format(re.escape(word)), title))
            if count > 0:
                if word in count_dict:
                    count_dict[word] += count
                else:
                    count_dict[word] = count

    after = data['data']['after']
    if after is None:
        sorted_words = sorted(
                count_dict.items(),
                key=lambda item: (-item[1], item[0])
                )
        for word, count in sorted_words:
            print("{}: {}".format(word, count))
    else:
        return count_words(subreddit, word_list, after, count_dict)
