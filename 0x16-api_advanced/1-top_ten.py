#!/usr/bin/python3

"""Module to interact with Reddit API."""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "subreddit-top-ten"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except KeyError:
        print(None)
