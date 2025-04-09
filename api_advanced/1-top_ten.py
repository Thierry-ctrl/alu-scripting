#!/usr/bin/python3
"""
Module that defines a function to query the Reddit API and print the titles
of the first 10 hot posts for a given subreddit.

If the subreddit is invalid (or if a redirect occurs), the function prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit to search.

    Returns:
        None. Prints the title for each post (one per line) if the subreddit exists,
        otherwise prints None.
    """
    url = (
        "https://www.reddit.com/r/{}/hot.json?limit=10"
        .format(subreddit)
    )
    headers = {
        "User-Agent": "python:1-top_ten:v1.0 (by /u/yourusername)"
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
        print(title)
