#!/usr/bin/python3

"""Module to interact with Reddit API."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Return a list of titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list of hot article titles (default is []).
        after (str): The "after" value for pagination (default is None).

    Returns:
        list: The list of hot article titles, or None if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "subreddit-hot-articles"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except KeyError:
        return None
