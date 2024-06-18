#!/usr/bin/python3

"""Module to interact with Reddit API."""

import requests
import re
from collections import Counter


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Print a sorted count of given keywords
    (case-insensitive) from titles of all hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to search for.
        hot_list (list): The list of hot article titles (default is []).
        after (str): The "after" value for pagination (default is None).

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "subreddit-keyword-counter"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"].lower())

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, hot_list, after)

        # Count keywords
        word_counts = Counter()
        for title in hot_list:
            words = re.findall(r'\b\w+\b', title)
            for word in words:
                if word in map(str.lower, word_list):
                    word_counts[word] += 1

        # Sum duplicates in word_list
        for word in set(word_list):
            count = sum(word_counts[w.lower()] for
                        w in word_list if w.lower() == word.lower())
            word_counts[word.lower()] = count

        # Sort and print results
        sorted_word_counts = sorted(word_counts.items(),
                                    key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            if count > 0:
                print(f"{word}: {count}")
    except KeyError:
        return
