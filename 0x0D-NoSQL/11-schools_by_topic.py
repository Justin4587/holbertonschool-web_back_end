#!/usr/bin/env python3
"""list all or empty"""


def schools_by_topic(mongo_collection, topic):
    """ the stuff"""
    mongo_collection.find({'topics': topic})

if __name__ == "__main__":
    schools_by_topic(mongo_collection, topics)
