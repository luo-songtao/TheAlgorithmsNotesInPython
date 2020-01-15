#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
哈希表：基于链接表
"""
import math

from hash_table import BaseHashTable


class HashTable(BaseHashTable):
     
    def _insert(self, key, value):
        hash_value = self.hash(key)
        linked_list = LinkedList() if self._slots[hash_value] is None else self._slots[hash_value]
        self._slots[hash_value] = linked_list
        linked_list.insert(Link(key, value))
        
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
                    

class Link:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return " {} ".format(self.key)


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def insert(self, link):
        if self.tail != None:
            self.tail.next = link
            link.prev = self.tail
        else:
            self.head = link
        self.tail = link
        
    def delete(self, link):
        if link.prev != None:
            link.prev.next = link.next
        else:
            self.head = link.next
        
        if link.next != None:
            link.next.prev = link.prev
        else:
            self.tail = link.prev
    
    def search(self, key):
        link = self.head
        while link != None and link.key != key:
            link = link.next
        return link   
    
    def traversal(self, reverse=False):
        link = self.head if reverse is False else self.tail
        while True:
            yield link
            if reverse is False and link.next != None:
                link = link.next
            elif reverse is True and link.prev != None:
                link = link.prev
            else:
                break   


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