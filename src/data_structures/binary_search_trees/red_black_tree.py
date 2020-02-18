#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from binary_search_tree import BinarySearchTreeNode as BaseNode
from binary_search_tree import BinarySearchTree as BaseBinarySearchTree


class RedBlackTreeNode(BaseNode):
    """红黑树节点
    
    相比二叉搜索树节点，增加了color属性
    
    Attributes:
        color: 节点颜色
    """
    
    def __init__(self, key):
        super(RedBlackTreeNode, self).__init__(key)
        self.color = None
    
    def __repr__(self):
        return "{}|{}".format(self.color, self.key)


class RedBlackTree(BaseBinarySearchTree):
    """红黑树
    
    红黑树是一颗满足以下性质的二叉搜索树：
        - 每个节点或是红色的、或是黑色的
        - 根节点是黑色的
        - 叶节点都是黑色的
        - 如果一个节点是红色的，则它的两个子节点都是黑色的
        - 对每个节点，从该节点到其所有后代叶节点的简单路径上，均包含相同数目的黑色节点

    红黑树确保没有一条路径会比其他路径长出2倍，因为它是近似于平衡的
    
    **一颗有n个内部节点的红黑树的高度至多为 :math:`2\lg (n+1)`**
    
    红黑树插入新节点：红黑树中插入新节点后，新节点颜色需要着为红色，同时为了保证红黑性质能继续保持，需要对树中相应的节点重新着色并旋转进行修复
    
    红黑树删除节点：红黑树删除节点后，同样为了保证红黑性质能继续保持，需要对树中相应的节点重新着色并旋转进行修复
    
    """
    
    RED = "red"
    BLACK = "black"
    
    def _insert(self, new_node):
        super()._insert(new_node)
        new_node.left = None
        new_node.right = None
        new_node.color = self.RED
        self._insert_fixup(new_node)
    
    def _insert_fixup(self, node):
        # 如果node是根节点，或者node的父节点是黑色的，那么根本不需要处理
        while node != self.root and node.parent.color == self.RED:
            if node.parent == node.parent.parent.left:
                the_parent_sibling_node = node.parent.parent.right
                if the_parent_sibling_node != None and the_parent_sibling_node.color == self.RED:    # 第一次循环必定满足条件
                    node.parent.color = self.BLACK
                    the_parent_sibling_node.color = self.BLACK
                    node.parent.parent.color = self.RED
                    node = node.parent.parent
                # 至少第二次循环才会执行下面的代码，是为了在保证性质5条件下，调整结构以重新满足性质4(详见相关书籍)
                elif node == node.parent.right:    
                    # 左旋：以调整为
                    #      red-node
                    #     /
                    #  red—node
                    # 这样的情形，从而让后面代码复用
                    node = node.parent
                    self.left_rotate(node)
                # 为了保证性质5，这里把node的父节点提升为新的根节点，把原本根节点(node.p.p)改为红色，并降级
                # 这样也就重新满足了性质4
                if node == self.root or node.parent == self.root:
                        break
                node.parent.color = self.BLACK
                node.parent.parent.color = self.RED
                self.right_rotate(node.parent.parent)
            else:    # 与前面逻辑相同，方向相反
                the_parent_sibling_node = node.parent.parent.left
                if the_parent_sibling_node != None and the_parent_sibling_node.color == self.RED:
                    node.parent.color = self.BLACK
                    the_parent_sibling_node.color = self.BLACK
                    node.parent.parent.color = self.RED
                    node = node.parent.parent
                elif node == node.parent.left:
                    node = node.parent
                    self.right_rotate(node)
                if node == self.root or node.parent == self.root:
                        break
                node.parent.color = self.BLACK
                node.parent.parent.color = self.RED
                self.left_rotate(node.parent.parent)
                
        self.root.color = self.BLACK
    
    def _delete(self, node):
        the_node = None
        original_color = node.color
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
            
            self.transplant(node, replacement_node)
            replacement_node.left = node.left
            replacement_node.left.parent = replacement_node
            
            original_color = replacement_node.color
            replacement_node.color = node.color
        if original_color == self.BLACK:    # 如果原来是红色，那么是不会破坏红黑树的性质，所以不需要修复
            self._delete_fixup(the_node)
        
    def _delete_fixup(self, node):
        """
        修复红黑树的性质
        """
        # 如果节点的颜色不是黑色，那么红黑树的性质没有被破坏：但需要把node颜色改为黑色，因为它顶替的节点原先颜色应该黑色(最后一行)
        while node != None and node != self.root and node.color == self.BLACK:
            # 使用枚举法，最后可以发现出规律：总结出来最终是有两种终极情况，而其他情况都可以通过左旋或右旋变换得出来
            # 具体查看相关书籍
            if node == node.parent.left:
                sibling_node = node.parent.right
                if sibling_node.color == self.RED:    # 即此时node.p.color 只能是黑色的情况
                    node.parent.color = self.RED
                    sibling_node.color = self.BLACK
                    self.left_rotate(node.parent)    # 此时原sibling_node已经是当前子树的根节点，颜色为黑色
                    sibling_node = node.parent.right     # 更新node的sibling_node
                
                # 终极情形1: 当同胞节点是黑色，父节点是红色时，如果同胞的左右孩子都是黑色时
                # 解决方案：让父节点变为黑色，同胞节点变为红色
                if sibing_node.left.color == self.BLACK and sibing_node.right.color == self.BLACK:
                    sibling_node.color = self.RED
                    node.parent.color = self.BLACK
                    break    # 已经解决，则可以退出循环
                    
                elif sibling_node.right.color == self.BLACK:    # 如果同胞节点的右孩子为黑色，左孩子为红色时
                    # 此时对同胞节点进行右旋，可以转换为第二种终极情形
                    # 但同时需要先将同胞节点和它的左孩子呼唤颜色
                    sibling_node.color = self.RED
                    sibling_node.left.color = self.BLACK
                    self.right_rotate(sibling_node)
                    # 此时再重新更新node 的同胞节点
                    sibling_node = node.parent.right
                
                # 如果终极情形1没出现，那么此时将出现终极情形2: 此时同胞节点为黑色，父节点为红色，同胞节点的右孩子为红色，左孩子为黑色
                # 解决方案：让父节点变为黑色，同胞节点变为红色;并把同胞节点的右孩子变为黑色；对父节点左旋
                node.parent.color = self.BLACK
                sibling_node.color = self.RED
                sibling_node.right.color = self.BLACK
                self.left_rotate(node.parent)
                break
            else:    # 逻辑相同，方向相反
                sibling_node = node.parent.left
                if sibling_node.color == self.RED:
                    node.parent.color = self.RED
                    sibling_node.color = self.BLACK
                    self.right_rotate(node.parent)
                    sibling_node = node.parent.left
                
                if sibling_node.right.color == self.BLACK and sibling_node.left.color == self.BLACK:
                    sibling_node.color = self.RED
                    node.parent.color = self.BLACK
                    break
                
                elif sibling_node.left.color == self.BLACK:
                    sibling_node.color = self.RED
                    sibling_node.right.color = self.BLACK
                    self.left_rotate(sibling_node)
                    sibling_node = node.parent.left
                
                node.parent.color = self.BLACK
                sibling_node.color = self.RED
                sibling_node.left.color = self.BLACK
                self.right_rotate(node.parent)
                break 
        node.color = self.BLACK    # 确保node颜色是黑色


if __name__ == "__main__":
    data = [13,6,12,5,19,7,20,99,11,3,9,38,15,5]
    
    red_black_tree = RedBlackTree()
    for i in data:
        red_black_tree.insert(RedBlackTreeNode(i))
    inorder = list(red_black_tree.traversal())
    print("中序遍历结果: ", inorder) 
    print("Minmum: ", red_black_tree.minimum(red_black_tree.root).key)
    print("Maximum: ", red_black_tree.maximum(red_black_tree.root).key)
    
    key = 6
    searched_node = red_black_tree.search(red_black_tree.root, key)
    print("Search node(key={}): ".format(key), None if searched_node is None else searched_node.key)
    
    print("删除node(key={})前的结果先序遍历结果: ".format(key), list(red_black_tree.traversal("preorder")))
    red_black_tree.delete(searched_node)
    print("删除node(key={})的结果先序遍历结果: ".format(key), list(red_black_tree.traversal("preorder")))
        
    