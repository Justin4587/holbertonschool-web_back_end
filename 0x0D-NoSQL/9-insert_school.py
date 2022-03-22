#!/usr/bin/env python3
"""list all or empty"""


def insert_school(mongo_collection, **kwargs):
    """ the stuff"""
    return mongo_collection.insert_one(kwargs)

if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
