#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


from hash_table import BaseHashTable, HashTableKeyError


class HashTableByOpenAdressing(BaseHashTable):
    """基于开放寻址方法的哈希表
    
    开放寻址方法的哈希表没有使用额外的容器存储元素，而是直接将元素存储在散列表的槽中。同时这里使用的是线性探查方法进行查找槽位。
    
    """

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
        """查询指定key值的元素并返回其value
        """
        result = self._search(key)
        return result if result is None else result[0]
        
    def __iter__(self):
        for item in self._slots:
            if item is not None:
                yield item


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../hashes/'))
    from numberic_hashes.multiplicative_hash import multiplicative_hash
    from string_hashes.elf import elf_hash
    
    table_size = 2**16
    hash_table = HashTableByOpenAdressing(table_size, multiplicative_hash, elf_hash)
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
    
