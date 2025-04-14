#!/usr/bin/python3
"""
Module to fetch and print the top 10 hot posts from a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of the first 10 hot posts for a subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
    
    Returns:
        None: Prints post titles or None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:subreddit.hot.posts:v1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if request was successful (status 200)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            
            if data:
                for post in data:
                    print(post.get("data", {}).get("title"))
            else:
                print("None")
        else:
            print("None")
    except Exception:
        print("None")
