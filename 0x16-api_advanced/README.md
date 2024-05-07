# Reddit API Interaction

This project contains Python functions that interact with the Reddit API:

1. `number_of_subscribers`:
    - Function prototype: `def number_of_subscribers(subreddit)`
    - Takes a subreddit name and returns the number of subscribers for that subreddit.
    - If the subreddit is invalid, it returns 0.

2. `top_ten`:
    - Function prototype: `def top_ten(subreddit)`
    - Takes a subreddit name and prints the titles of the first 10 hot posts.
    - If the subreddit is invalid, it prints None.

3. `recurse`:
    - Function prototype: `def recurse(subreddit, hot_list=[])`
    - Takes a subreddit name and returns a list of titles of all hot articles.
    - If the subreddit is invalid, it returns None.
    - The function is recursive and utilizes pagination to fetch all hot articles.

All functions are written in compliance with PEP 8 guidelines and utilize the Requests module for HTTP requests.
