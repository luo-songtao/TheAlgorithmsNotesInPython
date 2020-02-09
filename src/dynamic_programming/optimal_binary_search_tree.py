#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com-
"""
Author: luo-songtao
最优二叉搜索树： 每个节点的信息被搜索的概率不一，被搜索概率越高的节点信息应当离根节点越近，这样搜索的代价会更低
（深度+1）* 节点概率 = 该节点的搜索代价
"""
import math


def direct_recursion_optimal_bst(keys, fake_keys, i, j):
    """
    >>> keys= [(None, None), ("k1", 0.15), ("k2", 0.10), ("k3", 0.05), ("k4", 0.10), ("k5", 0.20)]
    >>> fake_keys = [("d0",0.05), ("d1", 0.10), ("d2", 0.05), ("d3", 0.05), ("d4", 0.05), ("d5", 0.10)]
    >>> direct_recursion_optimal_bst(keys, fake_keys, 1, 5)
    (2.75, 'k2')
    """

    if i == j+1:    # 没有关键字节点时
        return fake_keys[i-1][1], keys[i-1][0]
    elif i == j:    # 只有一个关键字节点时，伪关键字是根节点的子节点，所以有两倍的代价
        return keys[i][1] + 2*fake_keys[i-1][1] + 2*fake_keys[i][1], keys[i][0]
    else:
        the_cost = math.inf
        the_root = None
        for r in range(i, j+1):
            cost_left, _ = direct_recursion_optimal_bst(keys, fake_keys, i, r-1)
            cost_right, _ = direct_recursion_optimal_bst(keys, fake_keys, r+1, j)
            cost = cost_left + cost_right + \
                    sum([x[1] for x in keys[i:j+1]]) + \
                    sum([x[1] for x in fake_keys[i-1:j+1]])
            if cost < the_cost:
                the_cost = cost
                the_root = keys[r][0]
        return the_cost, the_root


def buttom_up_recursion_bst(keys, fake_keys, i, j):
    """
    >>> keys= [(None, None), ("k1", 0.15), ("k2", 0.10), ("k3", 0.05), ("k4", 0.10), ("k5", 0.20)]
    >>> fake_keys = [("d0",0.05), ("d1", 0.10), ("d2", 0.05), ("d3", 0.05), ("d4", 0.05), ("d5", 0.10)]
    >>> c, r = buttom_up_recursion_bst(keys, fake_keys, 1, 5)
    >>> c[(1,5)], r[(1,5)]
    (2.75, 'k2')
    """
    
    costs = {}
    roots = {}
    for i in range(1, len(keys)+1):
        costs[(i,i-1)] = fake_keys[i-1][1]
    
    for l in range(0, len(keys)-1):
        for i in range(1, len(keys)-l):
            j = i + l
            the_cost = math.inf
            the_root = None
            for r in range(i, j+1):
                cost = costs[(i, r-1)] + costs[(r+1, j)] + \
                    sum([x[1] for x in keys[i:j+1]]) + \
                    sum([x[1] for x in fake_keys[i-1:j+1]])
                if cost < the_cost:
                    the_cost = cost
                    the_root = keys[r][0]
            costs[(i,j)] = the_cost
            roots[(i,j)] = the_root
    return costs, roots

            
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    