#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
The Basic HashTable
"""
from numeric_hashes import numeric_hashes
from string_hashes import string_hashes


class BaseHashTable:
    
    def __init__(self, size, numeric_hash="multiplicative_hashing", string_hash="elf"):
        self.size = size
        self._slots = [None] * self.size
        self.numeric_hash = numeric_hashes[numeric_hash]
        self.string_hash = string_hashes[string_hash]
        self.count = 0
    
    def _insert(self, key, value):
        raise NotImplementedError
    
    def _delete(self, key):
        raise NotImplementedError
    
    def _search(self, key):
        raise NotImplementedError
    
    def __iter__(self):
        raise NotImplementedError

    def hash(self, key):
        if isinstance(key, str):
            key = self.string_hash(key)
        return self.numeric_hash(key, m=self.size)
    
    def insert(self, key, value):
        self._insert(key, value)
        self.count += 1

    def bulk_insert(self, items):
        for key, value in items:
            self.insert(key, value)
    
    def delete(self, key):
        self._delete(key)
        self.count -= 1
            
    def search(self, key):
        return self._search(key).value
    
    def rehash(self, factor=1):
        old_items = [item for item in self]
        self.count = 0
        self._slots.clear()
        self.size = factor * self.size
        self._slots = [None] * self.size
        self.bulk_insert(old_items)
    
    @property
    def load_factor(self):
        return round(self.count / self.size, 2)


class HashTableKeyError(BaseException):
    pass


