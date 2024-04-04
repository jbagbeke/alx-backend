#!/usr/bin/env python3
"""
Least Frequently Used (LRU) Caching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LRU Caching system with Base Caching as Base class
    """
    def __init__(self):
        """
        Constructor method
        """
        super().__init__()
        self.lfu_access = {}
        self.lfu_age = -1

    def put(self, key, item):
        """
        Stores Item in cache system
        """
        if key and item:
            self.cache_data[key] = item
            key_value = self.lfu_access.get(key)

            self.lfu_age += 1

            if len(self.cache_data) > super().MAX_ITEMS:
                # Extract a tuple of frequently accessed items
                # and corresponding lru values
                freq_vals = {key: (val[0]['freq_access'], val[1]['lru_access'])
                             for key, val in self.lfu_access.items()}

                # Extract tuple based on minimum freq_value and
                # lru in case of a tie between freq_values
                min_freq = min(freq_vals.items(),
                               key=lambda x: (x[1][0], x[1][1]))
                key_to_delete = min_freq[0]

                del self.cache_data[key_to_delete]
                del self.lfu_access[key_to_delete]

                print('DISCARD: {}'.format(key_to_delete))

            # Implementing a dict with keys having a list of dicts
            # as values - { key: [{freq_access: value}, {lru_acess: value}] }
            if key_value:
                key_value[0]['freq_access'] += 1
                key_value[1]['lru_access'] = self.lfu_age
            else:
                self.lfu_access[key] = [{'freq_access': 0},
                                        {'lru_access': self.lfu_age}]

    def get(self, key):
        """
        Returns Value of key specified
        """
        key_value = self.cache_data.get(key)

        if not key_value or not key:
            return None

        self.lfu_age += 1

        lfu_key_value = self.lfu_access.get(key)
        lfu_key_value[0]['freq_access'] += 1
        lfu_key_value[1]['lru_access'] = self.lfu_age

        return key_value
