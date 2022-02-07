#!/usr/bin/env python3
"""
    let the caching commence
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """somethings going to happen bets on Traceback??"""
    def __init__(self):
        self.cache_data = OrderedDict()

    temp = []

    def put(self, key, item):
        """ Im placing some generic text here """

        if key and item:
            if key not in self.temp:
                self.temp.append(key)
            else:
                self.temp.remove(key)
                self.temp.append(key)

            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstOut = self.temp.pop(-2)
            print("DISCARD: " + firstOut)
            del self.cache_data[firstOut]

    def get(self, key):
        """ bring me the keys"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.temp.remove(key)
            self.temp.append(key)
            return self.cache_data[key]
