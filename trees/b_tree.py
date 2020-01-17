#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
B树
"""

class Node:
    
    def __init__(self):
        self.leaf = True
        self.n = 0    # 节点关键词个数
        self.depth = 0
        self.keys = []
        self.child_nodes = []
    
    
class BTree:
    
    def __init__(self):
        self.root = None
        self.minmum_degree = None
    
    def allocate_node(self):
        """
        在O(1)的时间内为新节点分配一个磁盘页
        """
        return Node()

    def disk_read(self, node):
        """
        数据读取
        """
        pass
    
    def disk_write(self, node):
        """
        数据写入
        """
        pass

    def search(self, k):
        return self._search(self.root, k)
    
    def _search(self, node, k):
        """
        线性查找
        """
        for i in range(node.n):
            if k > node.keys[i]:
                i += 1
            elif k == node.keys[i]:
                return (node, i)
            else:
                break
        else:
            if node.leaf is True:
                return None
        child_node = self.disk_read(node)    # ???
        return slef._search(child_node, k)
    
    def create(self):
        node = self.allocate_node()
        node.leaf = True
        node.n = 0
        self.disk_write(node)
        self.root = node
    
    def split_child(self, node, i):
        pass
    