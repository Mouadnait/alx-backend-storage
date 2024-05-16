#!/usr/bin/env python3
"""Web.py"""

import requests
import redis
from time import sleep

# Initialize Redis client
r = redis.Redis(host='localhost', port=6379, db=0)

def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and cache the result with expiration.
    Also track the number of accesses to the URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    # Check if the page is cached
    cached_page = r.get(f"cache:{url}")
    if cached_page:
        return cached_page.decode('utf-8')
    
    # If not cached, fetch the page
    response = requests.get(url)
    html_content = response.text

    # Cache the result with an expiration time of 10 seconds
    r.setex(f"cache:{url}", 10, html_content)

    # Increment the access count
    r.incr(f"count:{url}")

    return html_content

# Bonus: Implementing with decorators
def cache_and_track(expiration: int):
    def decorator(func):
        def wrapper(url: str):
            # Check if the page is cached
            cached_page = r.get(f"cache:{url}")
            if cached_page:
                return cached_page.decode('utf-8')

            # If not cached, fetch the page
            html_content = func(url)

            # Cache the result with an expiration time
            r.setex(f"cache:{url}", expiration, html_content)

            # Increment the access count
            r.incr(f"count:{url}")

            return html_content
        return wrapper
    return decorator

@cache_and_track(expiration=10)
def get_page_decorated(url: str) -> str:
    """Fetch the HTML content of a URL without caching logic.
    
    Args:
        url (str): The URL to fetch.
    
    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text

# Example usage
if __name__ == "__main__":
    test_url = "http://slowwly.robertomurray.co.uk"
    
    # Using the non-decorated version
    print(get_page(test_url))
    
    # Sleep for a bit to see caching in action
    sleep(5)
    print(get_page(test_url))
    
    # Using the decorated version
    print(get_page_decorated(test_url))
    
    # Sleep for a bit to see caching in action
    sleep(5)
    print(get_page_decorated(test_url))
