# Project Name
**0x02. Redis basic**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240515%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240515T102349Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3fd38f288d5d049c3559c7237d0fe928c1aff767a8be4664a7ae49ff79ec5701)

## Resources
**Read or watch:**

-   [Redis Crash Course Tutorial](https://youtu.be/Hbt56gFj998?si=5Z3smI1miy16CNTg "Redis Crash Course Tutorial")
-   [Redis commands](https://redis.io/docs/latest/commands/ "Redis commands")
-   [Redis python client](https://redis-py.readthedocs.io/en/stable/ "Redis python client")
-   [How to Use Redis With Python](https://realpython.com/python-redis/ "How to Use Redis With Python")

## Learning Objectives

-   Learn how to use redis for basic operations
-   Learn how to use redis as a simple cache

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The first line of all your files should be exactly `#!/usr/bin/env python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).


## Install Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Project Description
Learn how to use redis for basic operations.
Learn how to use redis as a simple cache.

* **0. Writing strings to Redis** - Create a `cache` class with the given requirements. - `exercise.py`.
* **1. Reading from Redis and recovering original type** - Create a `get` method that takes a key string argument and an optional `Callable` argument named `fn`. - `exercise.py`.
* **2. Incrementing values** - Implement a system to count how many times methods of the `Cache` class are called. - `exercise.py`.
* **3. Storing lists** - Define a `call_history` decorator to store the history of inputs and outputs for a particular function. - `exercise.py`.
* **4. Retrieving lists** - Implement a `replay` function to display the history of calls of a particular function. - `web.py`.
