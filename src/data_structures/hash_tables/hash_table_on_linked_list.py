#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import math

from hash_table import BaseHashTable, HashTableKeyError


class HashTableOnLinkedList(BaseHashTable):
    """基于双向链表的hash表
    
    使用额外的双向链表存储hash表的元素
    
    """
     
    def _insert(self, key, value):
        hash_value = self.hash(key)
        linked_list = DoublyLinkedList() if self._slots[hash_value] is None else self._slots[hash_value]
        self._slots[hash_value] = linked_list
        linked_list.insert(DoublyLinkedListLink(key, value))
        
    def _delete(self, key):
        result = self._search(key)
        hash_value = self.hash(key)
        self._slots[hash_value].delete(result)
        if self._slots[hash_value].head == None:
            self._slots[hash_value] = None

    def _search(self, key):
        hash_value = self.hash(key)
        result = self._slots[hash_value] if self._slots[hash_value] is None \
                else self._slots[hash_value].search(key)
        if result is None:
            raise HashTableKeyError
        return result
    
    def __iter__(self):
        for i in self._slots:
            if i is not None:
                for item in i.traversal():
                    yield (item.key, item.value) 
                    

if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../linked_list/'))
    sys.path.insert(0, os.path.abspath('../../hashes/'))
    from doubly_linked_list import DoublyLinkedList, DoublyLinkedListLink
    from numberic_hashes.multiplicative_hash import multiplicative_hash
    from string_hashes.elf import elf_hash
    
    table_size = 2**16
    hash_table = HashTableOnLinkedList(table_size, multiplicative_hash, elf_hash)
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