#!/usr/bin/env python3
"""
    let the caching commence
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """somethings going to happen bets on Traceback??"""
    def __init__(self):
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Im placing some generic text here """

        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstOut = self.cache_data.popitem(last=False)
            print("DISCARD: " + str(firstOut[0]))

    def get(self, key):
        """ bring me the keys"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
