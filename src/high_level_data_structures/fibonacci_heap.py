#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import math


class FibonacciHeapNode:
    
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = None
        self.right = None
        self.mark = False


class FibonacciHeap:
    """斐波那契堆
    """
    
    def __init__(self):
        self.min: Node = None    # 最小节点
        self.heap_size = 0
            
    def create(self):
        pass
    
    def insert(self, node: FibonacciHeapNode):
        """插入新节点
        """
        node.degree = 0
        node.parent = None
        node.child = None
        node.mark = False
        if self.min == None:    # 如果堆为空
            # 建立根链表，且当前只有一个节点
            node.right = node
            node.left = node
            self.min = node
        else:
            # 将node添加到跟链表中
            node.right = self.min
            node.left = self.min.left
            self.min.left.right = node
            self.min.left = node
            if node.key < self.min.key:
                self.min = node
        self.heap_size += 1
    
    def minmum(self):
        """返回最小节点
        """
        if self.heap_size < 1:
            raise HeapUnderflowError
        return self.min
    
    def extract_min(self):
        """弹出最小节点
        """
        node = self.min
        if node != None:
            if node.child != None:
                # 将node的所有孩子添加到根链表中
                node.child.left.right = node.right
                node.child.left = node.left
            for i in range(node.degree):
                node.child.parent = None
                node.child = node.child.left
            if node == node.right:    # 处理只有一个节点的情况
                self.min = None
            else:
                # 随机设置一个最小节点，这里默认是node.right
                self.min = node.right
                # 重新调整堆
                self.consolidate()
            self.heap_size -= 1
        return node
    
    def get_max_degree(self):
        """计算具备size个节点的堆中，单个节点的最大度数(度数上界)
        """
        golden_ratio = (1+math.sqrt(5))/2
        return int(math.log(self.heap_size, golden_ratio))
            
    def consolidate(self):
        """合并根链表
        
        如果发现根链表中两个节点的度相等，那么就进行合并直到根链表中的节点的度两两不相等
        """
        max_degree = self.get_max_degree()
        # 记录degree的数值
        degree_record = [None for i in range(max_degree+1)]
        # 对根链表进行遍历
        node = self.min
        while node.right != self.min:
            the_degree = node.degree
            while degree_record[the_degree] != None:
                the_node = degree_record[the_degree]
                # 将key值高的节点从根节点移除并作为key值低的节点的子节点
                if node.key < the_node.key:
                    self.link(the_node, node)
                else:
                    self.link(node, the_node)
                degree_record[the_degree] = None
                the_degree += 1
            degree_record[the_degree] = node
            node = node.right
        self.min = None
        # 重置min node
        for i in range(max_degree+1):
            if degree_record[i] != None:
                if self.min == None:
                    self.min = degree_record[i]
                    self.min.left = self.min
                    self.min.right = self.min
                else:
                    node = degree_record[i]
                    node.right = self.min
                    node.left = self.min.left
                    self.min.left.right = node
                    self.min.left = node
                    if node.key < self.min.key:
                        self.min = node
        
    def link(self, x: FibonacciHeapNode, y: FibonacciHeapNode):
        """链接两个斐波那契堆
        
        实现步骤：
            1. remove node x from heap's root list
            2. make node x as a child of y, incrementing y.degree
            3. x.mark = False
        """
        # 1. ···
        x.left.right = x.right
        x.right.left = x.left
        
        # 2. ···
        if y.child != None:
            x.left = y.child.left
            x.right = y.child
            y.child.left.right = x
            y.child.left = x
        else:
            y.child = x
            x.left = x
            x.right = x
        x.parnet = y
        y.degree += 1
        # 3. ···
        x.mark = False
        
    def decrease_key(self, node, key):
        """减小node节点的关键值
        """
        if key > node.key:
            raise Exception("New key is greater than current key")
        node.key = key
        parent = node.parent
        if parent != None and node.key < parent.key:
            self.cut(node, parent)
            self.cascading_cut(parent)
        if node.key < self.min.key:
            self.min = node
    
    def cut(self, node: FibonacciHeapNode, parent: FibonacciHeapNode):
        """剪枝
        
        将node节点从当前子堆中剔除，并将node节点放入根链表作为一个根节点
        """
        # 
        if node.left == node:
            parent.child = None
        else:
            parent.child = node.left
        parent.degree -= 1
        # 
        node.parent = None
        node.mark = False
        node.left = self.min.left
        node.right = self.min
        self.min.left.right = node
        self.min.left = node
    
    def cascading_cut(self, node):
        """级联切断剪枝
        
        判断node节点是否已经是第二次失去子节点(如果mark==True)，如果是那么就要对它进行剪枝
        """
        if node.parent != None:    
            if node.mark == False:
                node.mark = True
            else:
                self.cut(node, node.parent)
                self.cascading_cut(node.parent)
                
    def delete(self, node: FibonacciHeapNode):
        """从堆中删除一个节点
        """
        self.decrease_key(node, -math.inf)
        self.extract_min()
    
    def union(self, heap):
        """合并两个FibonacciHeap为新的FibonacciHeap
        """
        return union(self, heap)
 
 
def union(h1: FibonacciHeap, h2: FibonacciHeap) -> FibonacciHeap:
    """合并斐波那契堆
    """
    heap = FibonacciHeap()    
    heap.min = h1.min
     
    temp_right = heap.min.right
    temp_left = h2.min.left
     
    temp_right.left = temp_left
    temp_left.right = temp_right
     
    heap.min.right = h2.min
    h2.min.left = heap.min
     
    if h2.min > h1.min:
        heap.min = h2.min
    heap.heap_size = h1.heap_size + h2.heap_size
    return heap


class HeapUnderflowError(BaseException):
    pass
