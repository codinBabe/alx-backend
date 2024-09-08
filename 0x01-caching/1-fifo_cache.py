#!/usr/bin/python3
"""A FIFO cache implementation"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFOCache class that inherits from BaseCaching and implements
    a first-in-first-out caching mechanism.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(first_in))
            self.cache_data.pop(first_in)

    def get(self, key):
        """Retrieve data from cache based on the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
