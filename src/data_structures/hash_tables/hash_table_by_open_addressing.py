#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
哈希表：开发寻址+线性探查
"""

from hash_table import BaseHashTable, HashTableKeyError


class HashTable(BaseHashTable):

    def _insert(self, key, value):
        hash_value = self.hash(key)
        for i in range(self.size):    # linear probing
            if self._slots[hash_value] is not None and self._slots[hash_value][0] != key:
                hash_value += 1
                if hash_value >= self.size:
                    hash_value = 0
            else:
                self._slots[hash_value] = (key, value)
                break

    def _delete(self, key):
        hash_value = self.hash(key)
        for i in range(self.size):
            if self._slots[hash_value] is None:
                raise HashTableKeyError
            elif self._slots[hash_value][0] == key:
                self._slots[hash_value] = None
                break
            else:
                hash_value += 1
                if hash_value >= self.size:
                    hash_value = 0
    
    def _search(self, key):
        hash_value = self.hash(key)
        for i in range(self.size):
            if self._slots[hash_value] is None:
                return None
            elif self._slots[hash_value][0] == key:
                return self._slots[hash_value]
            else:
                hash_value += 1
                if hash_value >= self.size:
                    hash_value = 0
    
    def search(self, key):
        result = self._search(key)
        return result if result is None else result[0]
        
    def __iter__(self):
        for item in self._slots:
            if item is not None:
                yield item


if __name__ == "__main__":
    table_size = 2**16
    hash_table = HashTable(table_size)
    data_size = 2**13
    data = [("k%d"%i, "v%d"%i) for i in range(data_size)]
    
    hash_table.bulk_insert(data)
    print("Load Factor(expect={}): ".format(round(data_size/table_size, 2)), hash_table.load_factor)
    key = "k1234"
    print("Search data(key='{}'): ".format(key), hash_table.search(key))
    
    hash_table.delete(key)
    print("Deleted data(key='{}'): ".format(key))

    try:
        print("Search data(key='{}'): ".format(key), hash_table.search(key))
    except HashTableKeyError:
        print("The data(key='{}') not in the hash table".format(key))
    rehash_factor = 2
    hash_table.rehash(2)
    print("Rehash by factor={}".format(rehash_factor))
    print("Load Factor(expect={}): ".format(round(data_size/(rehash_factor*table_size), 2)), hash_table.load_factor)
    
