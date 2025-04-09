#!/usr/bin/python3
"""
Module that defines a function to query the Reddit API and print the titles
of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.

    If the subreddit is invalid or encounters a redirect,
    prints None.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None. Prints each title on a new line if posts are found.
    """
    url = ("https://www.reddit.com/r/{}/hot.json?limit=10"
           .format(subreddit))
    headers = {
        "User-Agent": "python:1-top_ten:v1.0 (by /u/anonymous)"
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json()["data"]["children"]
    except (KeyError, ValueError):
        print(None)
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
