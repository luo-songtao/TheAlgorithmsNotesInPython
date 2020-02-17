#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from math import inf

the_graph = [
    [0,    3,    8,   inf,  -4 ],
    [inf,  0,    inf, 1,    7  ],
    [inf,  4,    0,   inf,  inf],
    [2,    inf,  -5,  0,    inf],
    [inf,  inf,  inf, 6,    0  ]
]


def transitive_closure(graph):
    """有向图的传递闭包
    
    有向图 :math:`G(V,E)` 的传递闭包指的是一个图 :math:`T(V, E^*)` ，如果G中有两个结点i,j之间存在一条路径，则  :math:`T(V, E^*)` 中结点i,j之间存在一条边 :math:`(i,j)\in E^*`
    
    计算有向图G的传递闭包，可以借助floyd-warshall算法，将每条给定边的权重设为1，然后使用floyd-warshall算法计算，如果结点i,j之间存在一条路径，则有 :math:`D_{ij}<n`，否则 :math:`D_{ij}= \infty` 
    
    图T的递归定义:
    
    .. math:: 
    
        T^{(0)}_{ij} = \left \{ \\begin{aligned} &0 \qquad &i!=j 且(i,j) \\notin E \\\\ &1 \\qquad & i==j 或(i,j) \in E \end{aligned} \\right.
    
    当 :math:`k\ge 1` 时:
    
    .. math:: T^{(k)}_{ij} = T^{(k-1)}_{ij} \space \\vert \space (T^{(k-1)}_{ij} \space \& \space T^{(k-1)}_{ij})
    
    Example:
        >>> from pprint import pprint
        >>> pprint(the_graph)
        [[0, 3, 8, inf, -4],
         [inf, 0, inf, 1, 7],
         [inf, 4, 0, inf, inf],
         [2, inf, -5, 0, inf],
         [inf, inf, inf, 6, 0]]
        >>> T = transitive_closure(the_graph)
        >>> pprint(T)
        [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]
    """
    n = len(graph)
    
    T = []
    for i in range(n):
        T.append([])
        for j in range(n):
            if graph[i][j] != inf:
                T[i].append(1)
            else:
                T[i].append(0)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] | (T[i][k] & T[k][j])
    return T


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    