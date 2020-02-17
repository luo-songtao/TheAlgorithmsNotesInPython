#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from math import inf
from copy import deepcopy


the_graph = [
    [0,    3,    8,   inf,  -4 ],
    [inf,  0,    inf, 1,    7  ],
    [inf,  4,    0,   inf,  inf],
    [2,    inf,  -5,  0,    inf],
    [inf,  inf,  inf, 6,    0  ]
]


def floyd_warshall(W):
    """结点对最短路径Floyd-Warshall算法
    
    Floyd-Warshall算法考虑的是图G的所有结点V :math:`\lbrace 1,2,3,...,n \\rbrace` 其中的一个子集 :math:`\lbrace 1,2,3,...,k \\rbrace` 。
    对于任意结点 :math:`i,j \in V` ，考虑从i到j的所有中间结点都取自 :math:`\lbrace 1,2,3,...,k \\rbrace` 的路径。
    
    Floyd-Warshall算法的时间复杂度是 :math:`O(n^3` 
    
    设 :math:`D^{k}_{ij}` 为从结点i到结点j的所有中间结点取自 :math:`\lbrace 1,2,3,...,k \\rbrace` 的一条最短路径的权重，:math:`D` 是对应的矩阵，则：
    
    .. math::
        
        D^{(k)}_{ij} = \left \{ \\begin{aligned} &\omega_{ij} \qquad &k=0 \\\\ &\min(D^{(k-1)}_{ij}, D^{(k-1)}_{ik} + D^{(k-1)}_{kj}) \qquad &k \ge 1  \end{aligned} \\right.
    
    Args:
        W: 表示 :math:`W` 矩阵，其中 :math:`\omega_{ij}` 表示边<i,j>的权重
    
    Example:
        >>> from pprint import pprint
        >>> pprint(the_graph)
        [[0, 3, 8, inf, -4],
         [inf, 0, inf, 1, 7],
         [inf, 4, 0, inf, inf],
         [2, inf, -5, 0, inf],
         [inf, inf, inf, 6, 0]]
        >>> D = floyd_warshall(the_graph)
        >>> pprint(D)
        [[0, 1, -3, 2, -4],
         [3, 0, -4, 1, -1],
         [7, 4, 0, 5, 3],
         [2, -1, -5, 0, -2],
         [8, 5, 1, 6, 0]]
    """
    
    n = len(W)
    D = deepcopy(W)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


if __name__ == '__main__':
    import doctest
    doctest.testmod()
