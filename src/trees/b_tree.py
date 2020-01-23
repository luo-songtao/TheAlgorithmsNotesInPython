#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
B树: 基于数组模拟B树的实现
"""

class Node:
    
    def __init__(self):
        self.leaf = True
        self.keys_count = 0    # 节点关键词个数
        self.depth = 0
        self.keys = []    # lenth = self.n
        self.child_nodes = []    # length = self.n + 1

    def get_key(self, i):
        return self.keys[i]
    
    def get_child_node(self, i):
        return self.child_nodes[i]
    
    def pop_key(self, i):
        return self.keys.pop(i)
    
    def pop_child_node(self, i):
        return self.child_nodes.pop(i)
    
    def insert_key(self, key, i=None):
        if i == None:
            self.keys.append(key)
        else:
            self.keys.insert(i, key)

    def insert_child_node(self, node, i=None):
        if i == None:
            self.child_nodes.append(node)
        else:
            self.child_nodes.insert(i, node)

class BTree:
    
    def __init__(self):
        self.root: Node = None
        self.minmum_degree = None
    
    def allocate_node(self) -> Node:
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

    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node: Node, key):
        """
        线性查找
        """
        for i in range(node.keys_count):
            if key > node.get_key(i):
                i += 1
            elif key == node.get_key(i):
                return (node, i)
            else:
                break
        if node.leaf is True:
            return None
        if i < node.keys_count:
            child_node = node.get_child_node(i)
        else:
            child_node = node.get_child_node(i+1)
        self.disk_read(child_node)    
        return slef._search(child_node, key)
    
    def create(self):
        node = self.allocate_node()
        node.leaf = True
        node.keys_count = 0
        self.disk_write(node)
        self.root = node
    
    def split_child(self, node: Node, i):
        """
        这里设定：子节点、关键词都是从0开始数，如第1个子节点实际上为第2个
        node节点第i个子节点达到2*self.minmum_degree-1个关键词，将要对其进行分裂，其第i个关键词提到node中
        第i个子节点的第self.minmum_degree, ... 第2*self.minmum_degree-1个关键词放入新节点中
        """
        the_child = node.get_child_node(i)
        if the_child.keys_count < self.minmum_degree - 1:
            raise Exception("未达到分裂条件")
        
        i_left_child = the_child
        i_right_child = self.allocate_node()
        i_right_child.leaf = i_left_child.leaf
        i_right_child.keys_count = self.minmum_degree - 1
        
        for _ in range(i_right_child.keys_count):    # 把后半部分的key移到新的节点
            i_right_child.insert_key(i_left_child.pop_key(self.minmum_degree))
            
        if not i_left_child.leaf:
            for _ in range(i_right_child.keys_count+1):    # 把后半部分的子节点指针移到新节点
                i_right_child.insert_child_node(i_left_child.pop_child_node(self.minmum_degree))
        
        node.insert_key(i, i_left_child.pop_key(self.minmum_degree-1))
        node.insert_child_node(i, i_left_child.pop_child_node(self.minmum_degree-1))
        
        node.keys_count += 1
        i_left_child.keys_count = self.minmum_degree - 1
        
        self.disk_write(node)
        self.disk_write(i_left_child)
        self.disk_write(i_right_child)
        
    def insert(self, key):
        node = self.root
        if node.keys_count == 2*self.minmum_degree - 1:
            new_node = self.allocate_node()
            self.root = new_node
            new_node.leaf = False
            new_node.keys_count = 0
            new_node.insert_child_node(node)
            self.split_child(new_node, 0)
            self._insert(new_node, key)
        else:
            self._insert(node, key)
    
    def _insert(self, node: Node, key):
        i = node.keys_count
        if node.leaf:
            while i >= 0 and key < node.get_key(i):
                i -= 1
            i += 1
            node.insert_key(i, key)
            node.keys_count += 1
        else:
            while i >= 0 and key < node.get_key(i):
                i -= 1
            i += 1
            the_child = node.get_child_node(i)
            self.disk_read(the_child)
            if the_child.keys_count == 2*self.minmum_degree - 1:
                self.split_child(node, i)
                if key > node.get_key(i):
                    the_child = node.get_child_node(i+1)
            self._insert(the_child, key)
    
    def delete(self, key):
        self._delete(self.root, key)
        
    def _delete(self, node: Node, key):
        pass
        
    