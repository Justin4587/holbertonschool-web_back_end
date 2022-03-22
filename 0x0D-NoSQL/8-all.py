#!/usr/bin/env python3
"""list all or empty"""


def list_all(mongo_collection):
    """list the stuff"""
    try:
        return mongo_collection.find()
    except:
        return []

if __name__ == "__main__":
    list_all(mongo_collection)
