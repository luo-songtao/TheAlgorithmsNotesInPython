#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from queue import PriorityQueue


class HuffmanCodeNode:
    
    def __init__(self, freq):
        self.freq = freq
        self.left = None
        self.right = None
        self.char = None    # if node is a leaf node

    def __repr__(self):
        return "{}:{}".format(self.char, self.freq)


def huffman_code(characters):
    """霍夫曼编码
    
    贪心选择：按字符出现频率最低次序的进行选择，来构建霍夫曼编码树
    
    时间复杂度: :math:`O(nlgn)`
    
    >>> characters = [("f", 5), ("e", 9), ("c", 12), ("b", 13), ("d", 16), ("a", 45)]
    >>> root_node = huffman_code(characters)
    >>> root_node
    None:100
    """
    queue = PriorityQueue()    # 优先级队列，lowest first
    for char, freq in characters:
        # 将每个字符初始化为一个叶节点，并按照字符频率压入优先级队列
        char_node = HuffmanCodeNode(freq)
        char_node.char = char
        queue.put((freq, char_node))
    
    for i in range(1, len(characters)):
        # 取出当前频率最低的两个节点
        left_node = queue.get()[1]
        right_node = queue.get()[1]
        # 构建新节点：以两个子节点的频率和作为该节点的频率值
        node = HuffmanCodeNode(left_node.freq+right_node.freq)
        node.left = left_node
        node.right = right_node
        # 再压入优先级队列中
        queue.put((node.freq, node))
    # 由于前面进行了n-1此循环，因此最后还剩下一个元素，它就是树的根节点
    return queue.get()[1]
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    