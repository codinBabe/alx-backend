#!/usr/bin/python3
""" MRU Caching"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache system """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.mru.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru.pop()
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))
        self.cache_data[key] = item
        self.mru.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.mru.remove(key)
        self.mru.append(key)
        return self.cache_data[key]