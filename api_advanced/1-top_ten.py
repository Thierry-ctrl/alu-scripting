#!/usr/bin/python3
"""
Module that defines a function to query the Reddit API and print the
titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.
    If the subreddit is invalid or a redirect occurs, prints None.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        None. Prints each post title on a new line, or prints None on error.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = (
        "https://www.reddit.com/r/{}/hot.json?limit=10"
        .format(subreddit)
    )
    headers = {"User-Agent": "HolbertonSchool"}

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    if not posts:
        print(None)
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
