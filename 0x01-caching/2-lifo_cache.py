#!/usr/bin/env python3
"""
LIFO Caching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching Class with Base Caching as Base class
    """

    def __init__(self):
        """
        Constructor method
        """
        super().__init__()
        self.last_put_key = None

    def put(self, key, item):
        """
        Stores Item in cache system
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > super().MAX_ITEMS:
                del self.cache_data[self.last_put_key]
                print('DISCARD: {}'.format(self.last_put_key))
            self.last_put_key = key

    def get(self, key):
        """
        Returns Value of key specified
        """
        key_value = self.cache_data.get(key)

        if not key_value or not key:
            return None

        return key_value
