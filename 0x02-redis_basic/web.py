#!/usr/bin/env python3
"""Module for implementing an expiring web cache and tracker
"""
import requests
from functools import wraps
from redis import Redis as R
from typing import Callable


def count_url(method: Callable) -> Callable:
    """_summary_
    count_url : count
    how many times a url is accessed        
    """
    @wraps(fn)
    def wrapper(url):
        """_summary_

        Returns:
            _type_: _description_
        """
        cached_url = f'cached:{url}'
        cached_data = R.get(cached_url)
        if cached_data:
            return cached_data.decode('utf-8')
        count_key = f'count:{url}'
        html_cont = method(url)

        R.incr(count_key)
        R.set(cached_url, html_cont)
        R.expire(cached_url, 10)
        return html_cont
    return wrapper


@count_url
def get_page(url: str) -> str:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        str: _description_
        html content of a given url
    """
    resp = requests.get(url)
    return resp.text
