#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


class DisjoinSet:
    """不相交集合-森林
    """
    
    def __init__(self):
        """实现中使用字典维护集合中元素的关系
        """
        self.items = {}
    
    def make(self, x):
        """创建新的集合
        """
        self.items[x] = {
            "parent": x,
            "rank": 0
        }
    
    def find_set(self, x):
        """
        使用路径压缩的方式
        """
        if x != self.items[x]["parent"]:
            self.items[x]["parent"] = self.find_set(self.items[x]["parent"])
        return self.items[x]["parent"]
    
    def union(self, x, y):
        x = self.find_set(x)
        y = self.find_set(y)
        
        if self.items[x]["rank"] > self.items[y]["rank"]:
            self.items[y]["parent"] = x
        else:
            self.items[x]["parent"] = y
            if self.items[x]["rank"] == self.items[y]["rank"]:
                self.items[y]["rank"] += 1
