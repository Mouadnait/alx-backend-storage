#!/usr/bin/env python3
"""Module for task 0

Create a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis (using redis.Redis()) and
flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the input
data in Redis using the random key and return the key.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called.

    Args:
        method: The method to decorate.

    Returns:
        Callable: A decorated version of the method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that adds input and output history to Redis.

        Returns:
            The output of the original function.
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that stores the history of inputs and outputs for a
    particular function in Redis.

    Args:
        method (Callable): A callable that represents the original
        function to be decorated.

    Returns:
        Callable: A new callable that wraps the original function
        and adds input and output history to Redis.
    """
    inputs = method.__qualname__ + ':inputs'
    outputs = method.__qualname__ + ':inputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function that adds input and output history to Redis.

        Returns:
            The output of the original function.
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper

def replay(method: Callable) -> None:
    """Displays the history of calls of a particular function.

    Args:
        fn (callable): The function whose history of calls is to be
        displayed.

    Returns:
        None
    """
    inputs = f'{method.__qualname__}:inputs'
    outputs = f'{method.__qualname__}:outputs'

    in_el = method.__self__._redis.lrange(inputs, 0, -1)
    out_el = method.__self__._redis.lrange(outputs, 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(in_el)))
    for i, o in zip(in_el, out_el):
        print(
            f"{method.__qualname__}\
                (*{i.decode('utf-8')}) \
                    -> {o.decode('utf-8')}"
            )


class Cache:
    """Cache class.
    """

    def __init__(self):
        """Cache class constructor that initializes a Redis client instance
        and flushes the database with flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method to store data in Redis and return a key for the stored
        data.

        Args:
            data (Union[str, bytes, int, float]): The data to store. Can
            be a str, bytes, int, or float.

        Returns:
            str: A randomly generated key that can be used to retrieve
            the stored data.
        """
        # generate a random key using uuid
        key = str(uuid.uuid4())
        # store the data in Redis using the key
        self._redis.set(key, data)
        # return the key
        return key

    def get(self, key, fn=None) -> Union[str, bytes, int, float]:
        """Method to get data from Redis and optionally apply a conversion
        function to the retrieved data.

        Args:
            key (str): The key used to store the data in Redis.
            fn (Optional): An optional callable that is used to convert the
            retrieved data to the desired format. Defaults to None.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data,
            optionally converted to the desired format.
        """
        if fn is None:
            return self._redis.get(key)
        return fn(self._redis.get(key))

    def get_str(self, key) -> Optional[str]:
        """Method to get a string from Redis.

        Args:
            key: The key used to store the string in Redis.

        Returns:
            Optional[str]: The retrieved string or None if the key does not
            exist.
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Optional[int]:
        """Method to get an integer from Redis.

        Args:
            key: The key used to store the integer in Redis.

        Returns:
            Optional[int]: The retrieved integer or None if the key does not
            exist.
        """
        # use get with a conversion function to retrieve an integer
        return self.get(key, int)
