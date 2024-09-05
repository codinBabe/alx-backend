#!/usr/bin/python3
"""A LIFO cache implementation"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO (Last-In, First-Out) cache implementation"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_in = list(self.cache_data.keys())[-1]
                print("DISCARD: {}".format(last_in))
                self.cache_data.pop(last_in)
        self.cache_data[key] = item
        self.cache_data[key] = self.cache_data.pop(key)
    
    def get(self, key):
        """Retrieve data from cache based on the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]