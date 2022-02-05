#!/usr/bin/env python3
"""
    let the caching commence
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """somethings going to happen bets on Traceback??"""
    temp = []

    def put(self, key, item):
        """ Im placing some generic text here """

        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                firstOut = self.temp.pop(0)
                print("DISCARD: " + firstOut)
                del self.cache_data[firstOut]

            if key not in self.temp:
                self.temp.append(key)

            self.cache_data[key] = item

    def get(self, key):
        """ bring me the keys"""
        return self.cache_data.get(key)
