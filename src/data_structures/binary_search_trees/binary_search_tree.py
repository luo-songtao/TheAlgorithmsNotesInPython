#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com

class BinarySearchTreeNode:
    """树节点对象
    
    Attributes:
        parent: 父节点，默认为None
        left: 左子节点，默认为None
        right: 右子节点，默认为None
        key: 节点上存储的关键值
    """
    
    def __init__(self, key):
        """
        Args:
            key (int): 节点存储的关键字值
        """
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
    
    def __repr__(self):
        return str(self.key)


class BinarySearchTree:
    """二叉搜索树
    
    Attributes:
        root: 父节点，默认为None
        count: 节点数，默认为0
        depth: 树高度，默认为0
    """
    
    def __init__(self):
        self.root = None
        self.count = 0
        self.depth = 0
    
    def _insert(self, new_node: BinarySearchTreeNode):
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

        
    def insert(self, node):
        """将新节点插入二叉搜索树中，将作为新的叶子节点
        
        Args:
            new_node (BinarySearchTreeNode): 新节点对象
        """
        self._insert(node)
        self.count += 1
    
    def delete(self, node):
        """删除当前树中的node节点，并调整树的相关节点以保持二叉搜索树的性质
        
        Args:
            node (BinarySearchTreeNode): 将要删除的节点
        
        """
        self._delete(node)
        self.count -= 1
    
    def search(self, node: BinarySearchTreeNode, key: int):
        """从指定节点开始搜索关键值为key的节点并返回
        
        Args:
            node (BinarySearchTreeNode): 要寻找的树或子树的根节点
            key (int): 要寻找的节点的关键值
        """
        while node != None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node
    
    def is_empty(self):
        """判断树是否为空
        """
        return True if self.root is None else False
    
    def minimum(self, node):
        """从指定节点开始获取其子树中关键值最小的节点
        
        Args:
            node (BinarySearchTreeNode): 要查找的树或子树的根节点
        """
        while node.left != None:
            node = node.left
        return node

    def maximum(self, node):
        """从指定节点开始获取其子树中关键值最大的节点
        
        Args:
            node (BinarySearchTreeNode): 要查找的树或子树的根节点
        """
        while node.right != None:
            node = node.right
        return node

    def traversal(self, order="inorder"):
        """遍历
        
        按指定的方式遍历树。先序("preorder")、中序("postorder")、后序("inorder")。
        
        Args:
            order (str):  遍历方式。默认"inorder"
        
        Returns:
            生成器
        
        """
        if order == "preorder":
            yield from self.preorder_tree_walk(self.root)
        elif order == "postorder":
            yield from self.postorder_tree_walk(self.root)
        else:
            yield from self.inorder_tree_walk(self.root)
    
    def transplant(self, node, transplanted_node):
        """节点移植
        
        将transplanted_node移植到node节点位置。主要处理父节点与其的关系
            - 设置node的父节点是transplanted_node的新父节点
            - 设置node的父节点的对应孩子是transplanted_node

        Args:
            node (BinarySearchTreeNode): 原节点
            transplanted_node (BinarySearchTreeNode): 移植节点
        
        """
        if node.parent == None:
            self.root = transplanted_node
        elif node == node.parent.left:
            node.parent.left = transplanted_node
        else:
            node.parent.right = transplanted_node
        if transplanted_node != None:
            transplanted_node.parent = node.parent
            
    def left_rotate(self, old_root):
        r"""子树左旋
        
        left rotate(左旋)：(这里root指树的根节点或子树的根节点)
        
        左旋和右旋是一种可以保持二叉搜索树性质的搜索树局部操作
        
        左旋示意图:
        .. math::
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
        r"""子树右旋
        
        right rotate(右旋)：(这里root指树的根节点或子树的根节点)

        左旋和右旋是一种可以保持二叉搜索树性质的搜索树局部操作
        
        右旋示意图:
        .. math::
                    old_root
                   /        \
                new_root     c
                /       \
               a         b 
            -----------------------
                new_root
               /        \
              a           old_root
                        /         \
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
    
    root_node = BinarySearchTreeNode(13)
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(root_node)
    for i in data:
        binary_search_tree.insert(BinarySearchTreeNode(i))
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