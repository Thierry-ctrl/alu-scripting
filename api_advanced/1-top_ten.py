#!/usr/bin/python3
"""
Module that defines a function to query the Reddit API and print the titles
of the first 10 hot posts for a given subreddit.

The function, top_ten(subreddit), uses the Reddit JSON API endpoint.
If the subreddit is invalid, it prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit to search.

    Returns:
        None. Prints the titles of the posts (one per line) or None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {})
    posts = data.get('children', [])

    for post in posts[:10]:
        title = post.get('data', {}).get('title')
        print(title)
