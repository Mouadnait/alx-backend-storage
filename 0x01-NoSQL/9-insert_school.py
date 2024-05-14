#!/usr/bin/env python3
"""task 9"""


def insert_school(mongo_collection, **kwargs):
    '''function that inserts a new document
    in a collection based on kwargs'''
    id = mongo_collection.insert_one(kwargs)
    return id.inserted_id
