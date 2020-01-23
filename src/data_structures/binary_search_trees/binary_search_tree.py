#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
基本的二叉搜索树
"""


class Node:
    
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
    
    def __repr__(self):
        return str(self.key)
        

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.count = 0
        self.depth = 0
    
    def _insert(self, new_node):
        """
        将新节点放置进二叉搜索树中，作为新的叶子节点（注意：新节点将是新的叶节点）
        """
        the_node = None
        temp = self.root    # 从根节点向下找
        
        while temp != None:    # 一直找到叶子节点
            the_node = temp
            if new_node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        # 然后把新节点作为新的叶子节点，原先的叶子节点变成了它的父节点
        new_node.parent = the_node
        if the_node == None:
            self.root = new_node
        elif new_node.key < the_node.key:
            the_node.left = new_node
        else:
            the_node.right = new_node
    
    def _delete(self, node):
        """
        删除当前树中删除node节点，并调整树的相关节点以保持二叉搜索树的性质
        """
        if node.left == None:    # 只有一个孩子时，那么就直接让他来上位，这样所有后代都会满意，所以只用考虑父亲的感受
            self.transplant(node, node.right) 
        elif node.right == None:   # 同理
            self.transplant(node, node.left)
        # 前两个已经包括了根本没有孩子的情况，node.right=None,同时node.left=None
        else:    
            # 当左右孩子都存在时，为了照顾左右的所有后代
            # 则需要从左边找个最大的或从右边找个最小的后代，来重新管理这帮孩子
            replacement_node = self.minimum(node.right)    # 这里从右边找最小的来
            
            # 如果找的后代和node不是直接的父子关系，那么需要让这个后代先把原先的关系安顿好了
            if replacement_node.parent != node:
                self.transplant(replacement_node, replacement_node.right)
                replacement_node.right = node.right    
                replacement_node.right.parent = replacement_node
            
            self.transplant(node, replacement_node)
            replacement_node.left = node.left
            replacement_node.left.parent = replacement_node

    def transplant(self, old_child_node, new_child_node):
        """
        当要删除old_child_node并用new_child_node进行替换时
        用于建立old_child_node的父节点与new_child_node之间的关系
        (交代：your parent will be my parent)
        """
        if old_child_node.parent == None:
            self.root = new_child_node
        elif old_child_node == old_child_node.parent.left:
            old_child_node.parent.left = new_child_node
        else:
            old_child_node.parent.right = new_child_node
        if new_child_node != None:
            new_child_node.parent = old_child_node.parent
            
    def left_rotate(self, old_root):
        """
        left rotate(左旋)：(这里root指树的根节点或子树的根节点)
                old_root
               /        \
              a           new_root
                        /         \
                       b            c
            -----------------------
                new_root
               /        \
            old_root     c
            /       \
           a         b 
        """
        new_root = old_root.right
        # 1. 新根节点交出左孩子
        old_root.right = new_root.left
        if new_root.left != None:
            new_root.left.parent = old_root
        # 2. 交代父节点与新根节点的关系
        new_root.parent = old_root.parent
        if old_root.parent == None:
            self.root = new_root
        elif old_root.parent.left == old_root:
            old_root.parent.left = new_root
        else:
            old_root.parent.right = new_root
        # 3. 互相变更关系：子变父，父变子
        new_root.left = old_root
        old_root.parent = new_root

    def right_rotate(self, old_root):
        """
        right rotate(右旋)：(这里root指树的根节点或子树的根节点)
                    old_root
                   /        \\
                new_root     c
                /       \\
               a         b 
            -----------------------
                new_root
               /        \\
              a           old_root
                        /         \\
                       b            c
        """ 
        new_root = old_root.left
        
        old_root.left = new_root.right
        if new_root.right != None:
            new_root.right.parent = old_root
        new_root.parent = old_root.parent
        if old_root.parent == None:
            self.root = new_root
        elif old_root.parent.left == old_root:
            old_root.parent.left = new_root
        else:
            old_root.parent.right = new_root
        new_root.right = old_root
        old_root.parent = new_root
    
    def insert(self, node):
        self._insert(node)
        self.count += 1
    
    def delete(self, node):
        self._delete(node)
        self.count -= 1
    
    def search(self, node, key):
        while node != None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node
    
    def is_empty(self):
        return True if self.root is None else False
    
    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node

    def traversal(self, order="inorder"):
        if order == "preorder":
            yield from self.preorder_tree_walk(self.root)
        elif order == "postorder":
            yield from self.postorder_tree_walk(self.root)
        else:
            yield from self.inorder_tree_walk(self.root)
    
    @classmethod
    def inorder_tree_walk(cls, node):
        if node != None:
            yield from cls.inorder_tree_walk(node.left)
            yield node
            yield from cls.inorder_tree_walk(node.right)
    
    @classmethod
    def preorder_tree_walk(cls, node):
        if node != None:
            yield node
            yield from cls.preorder_tree_walk(node.left)
            yield from cls.preorder_tree_walk(node.right)
    
    @classmethod
    def postorder_tree_walk(cls, node):
        if node != None:
            yield from cls.preorder_tree_walk(node.left)
            yield from cls.preorder_tree_walk(node.right)
            yield node
    

if __name__ == "__main__":
    
    data = [6,12,5,19,7,20,99,11,3,9,38,15,5]
    
    root_node = Node(13)
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(root_node)
    for i in data:
        binary_search_tree.insert(Node(i))
    inorder = list(binary_search_tree.traversal())
    print("中序遍历结果: ", inorder) 
    print("Minmum: ", binary_search_tree.minimum(binary_search_tree.root).key)
    print("Maximum: ", binary_search_tree.maximum(binary_search_tree.root).key)
    
    key = 13
    searched_node = binary_search_tree.search(binary_search_tree.root, key)
    print("Search node(key={}): ".format(key), None if searched_node is None else searched_node.key)
    
    print("删除node(key={})前的结果先序遍历结果: ".format(key), list(binary_search_tree.traversal("preorder")))
    binary_search_tree.delete(searched_node)
    print("删除node(key={})的结果先序遍历结果: ".format(key), list(binary_search_tree.traversal("preorder")))