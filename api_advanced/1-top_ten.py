#!/usr/bin/python3

"""
Displays the titles of 10 hot posts listed for a subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    The Function that fethces the Reddit API
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
