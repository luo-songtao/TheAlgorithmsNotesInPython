#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from binary_search_tree import BinarySearchTreeNode as BaseNode
from binary_search_tree import BinarySearchTree as BaseBinarySearchTree


class AVLTreeNode(BaseNode):
    """平衡二叉树节点
    
    相比二叉搜索树节点，增加了height属性
    
    Attributes:
        height: 记录当前节点在树中所在的高度
    """
    
    def __init__(self, key):
        super(AVLTreeNode, self).__init__(key)
        self.height = 1
    
    def __repr__(self):
        return "{}(h={})".format(self.key, self.height)

class AVLTree(BaseBinarySearchTree):
    """平衡二叉树
    
    平衡二叉树一种高度平衡的二叉搜索树。对于树中每一个节点，它的左右子树的高度差至多为1.
    
    """
    
    def _insert(self, new_node):
        super()._insert(new_node)
        self._insert_balance_fixup(new_node)
    
    def _insert_balance_fixup(self, node):
        while node != self.root and node != None:
            if node == node.parent.left:
                if node.parent.right == None and node.height == 1:
                    node.parent.height += 1
                elif node.parent.right == None:
                    self.right_rotate(node.parent)
                    node.right.height = node.height - 1
                elif node.height - node.parent.right.height >= 2:
                    self.right_rotate(node.parent)
                    node.right.height = node.height - 1
                elif node.height > node.parent.right.height:
                    node.parent.height = node.height + 1
                node = node.parent
            else:
                if node.parent.left == None and node.height == 1:
                    node.parent.height += 1
                elif node.parent.left == None:
                    self.left_rotate(node.parent)
                    node.left.height = node.height - 1
                elif node.height - node.parent.left.height >= 2:
                    self.left_rotate(node.parent)
                    node.left.height = node.height - 1
                elif node.height > node.parent.left.height:
                    node.parent.height = node.height + 1
                node = node.parent

    def _delete(self, node):
        if node.left == None:
            the_node = node.right
            self.transplant(node, node.right) 
        elif node.right == None: 
            the_node = node.left
            self.transplant(node, node.left)
        else:    
            replacement_node = self.minimum(node.right) 
            the_node = replacement_node.right
            if replacement_node.parent != node:
                self.transplant(replacement_node, replacement_node.right)
                replacement_node.right = node.right    
                replacement_node.right.parent = replacement_node
                replacement_node.height = node.height
            
            self.transplant(node, replacement_node)
            replacement_node.left = node.left
            replacement_node.left.parent = replacement_node
        self._delete_balance_fixup(the_node)
    
    # def _delete_balance_fixup(self, the_node):
    #     """
    #     :params node: 
    #     """
    #     while node != self.root:
    #         if node == None:
                
    #         if node == node.parent.right:
                
                    
            
        
    

if __name__ == "__main__":
    avl_tree = AVLTree()
    for i in range(10):
        avl_tree.insert(AVLTreeNode(i))
    print("中序遍历结果: ", list(avl_tree.traversal())) 
    print("先序遍历结果: ", list(avl_tree.traversal("preorder"))) 
    print("Minmum: ", avl_tree.minimum(avl_tree.root).key)
    print("Maximum: ", avl_tree.maximum(avl_tree.root).key)
    
    key = 5
    searched_node = avl_tree.search(avl_tree.root, key)
    print("Search node(key={}): ".format(key), None if searched_node is None else searched_node.key)
    
    print("删除node(key={})前的结果先序遍历结果: ".format(key), list(avl_tree.traversal("preorder")))
    avl_tree.delete(searched_node)
    print("删除node(key={})的结果先序遍历结果: ".format(key), list(avl_tree.traversal("preorder")))