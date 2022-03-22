#!/usr/bin/env python3
"""list all or empty"""


def insert_school(mongo_collection, **kwargs):
    """ the stuff"""
    coll = {}
    for k, v in kwargs.items():
        coll[k] = v
    docId = mongo_collection.insert_one(coll)
    return docId

if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
