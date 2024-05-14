#!/usr/bin/env python3
"""task 8"""


def list_all(mongo_collection):
    """function that lists all
    documents in a collection"""
    if mongo_collection is None:
        return []
    return mongo_collection.find()
