#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


class BaseHashTable:
    """基本哈希表
    
    Attributes:
        size: 哈希表大小上限
        numberic_hash: 数值hash函数
        string_hash: 字符串hash函数
        count: 哈希表中已存放数据条目数
    """
    
    def __init__(self, size, numberic_hash, string_hash):
        """
        Args:
            size: 哈希表大小上限
            numberic_hash: 数值hash函数
            string_hash: 字符串hash函数
        """
        self.size = size
        self._slots = [None] * self.size
        self.numberic_hash = numberic_hash
        self.string_hash = string_hash
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
        """根据指定key计算hash值
        
        如果key是字符串将使用字符串函数；如果是数值，将使用数值hash函数
        
        """
        if isinstance(key, str):
            key = self.string_hash(key)
        return self.numberic_hash(key, m=self.size)
    
    def insert(self, key, value=None):
        """插入数据
        
        Args:
            key: 字符串或数值类型的关键值
            value: 存放的数据，默认是None
        """
        self._insert(key, value)
        self.count += 1

    def bulk_insert(self, items):
        """批量插入数据
        
        Args:
            items: 由二元元组(key, value)组成的可迭代对象
        """
        for key, value in items:
            self.insert(key, value)
    
    def delete(self, key):
        """从hash表中删除指定key值的元素
        """
        self._delete(key)
        self.count -= 1
            
    def search(self, key):
        """查询指定key值的元素并返回其value
        """
        return self._search(key).value
    
    def rehash(self, factor=2):
        """重新分配hash表存储空间大小，默认将大小扩大1倍
        
        Args:
            factor: rehash因子，默认为2
        
        """
        old_items = [item for item in self]
        self.count = 0
        self._slots.clear()
        self.size = factor * self.size
        self._slots = [None] * self.size
        self.bulk_insert(old_items)
    
    @property
    def load_factor(self):
        """hash表装载因子
        """
        return round(self.count / self.size, 2)


class HashTableKeyError(BaseException):
    pass


