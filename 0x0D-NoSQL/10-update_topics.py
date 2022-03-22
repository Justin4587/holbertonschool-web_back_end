#!/usr/bin/env python3
"""list all or empty"""


def update_topics(mongo_collection, name, topics):
    """ the stuff"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})

if __name__ == "__main__":
    update_topics(mongo_collection, name, topics)
