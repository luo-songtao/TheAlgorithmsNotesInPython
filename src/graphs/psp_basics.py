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


class GeneralPairsShortestPaths:
    """一般的结点对最短路径算法
    
    有向图上所有节点对最短路径问题可以使用动态规划算法:
        - 最短路径的结构：一条最短路径的所有子路径都是最短路径
        - 所有结点对最短路径问题的递归解：
            - 设 :math:`l^{(m)}_{ij}`为从i结点到j结点的至多包含m多条边的任意路径的最小权重，并用矩阵 :math:`L^{(m)}`存储。当m=0时，也就是i结点到j结点没有之间没有便，有两种情况，一种是i=j,( :math:`l^{(m)}_{ij}=0`)，另一种是i和j不连通( :math:`l^{(m)}_{ij}=\inf`)。且有：
            .. math:: l^{(m)}_{ij} = \min (l^{(m-1)}_{ij}, \min_{1\le k \le n} \{l^{(m-1)}_{ik}+\omega_{kj} \}  
    
    这里我们默认有向图使用矩阵形式表示，只记录权重的矩阵记为 :math:`W`，其中:math:`\omega_{ij}`表示边<i,j>的权重
    """
    @classmethod
    def extend_shortest_paths(cls, L, W, P=None):
        """
        根据 :math:`L^{m-1}` 计算 :math:`L^{(m)}`
        
        .. math:: l^{(m)}_{ij} = \min (l^{(m-1)}_{ij}, \min_{1\le k \le n} \{l^{(m-1)}_{ik}+\omega_{kj} \}
        
        Args:
            L: 表示 :math:`L^{m-1}` 矩阵
            W: 表示 :math:`W` 矩阵，其中 :math:`\omega_{ij}` 表示边<i,j>的权重
            P: 表示 :math:`L^{m-1}` 的前驱子图矩阵，记录结点的前驱
        """
        n = len(W)
        L_m = L
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    l_ij = min(L_m[i][j], L_m[i][k] + W[k][j])
                    if l_ij != L_m[i][j]:
                        L_m[i][j] = l_ij
                        if P is not None:
                            P[i][j] = k
        return L_m, P

    @classmethod
    def slow_pairs_shortest_paths(cls, W):
        """较慢的计算版本
        
        运算复杂度为 :math:`O(n^4)`
        
        Args:
            W: 表示 :math:`W` 矩阵，其中 :math:`\omega_{ij}` 表示边<i,j>的权重
        
        Retuens:
            L矩阵, P矩阵
            
        Example:
            >>> from pprint import pprint
            >>> pprint(the_graph)
            [[0, 3, 8, inf, -4],
             [inf, 0, inf, 1, 7],
             [inf, 4, 0, inf, inf],
             [2, inf, -5, 0, inf],
             [inf, inf, inf, 6, 0]]
            >>> L_m, P = GeneralPairsShortestPaths.slow_pairs_shortest_paths(the_graph)
            >>> pprint(L_m)
            [[0, 1, -3, 2, -4],
             [3, 0, -4, 1, -1],
             [7, 4, 0, 5, 3],
             [2, -1, -5, 0, -2],
             [8, 5, 1, 6, 0]]
            >>> pprint(P)
            [[None, 2, 3, 4, 0],
             [3, None, 3, 1, 0],
             [3, 2, None, 1, 0],
             [3, 2, 3, None, 0],
             [3, 2, 3, 4, None]]
        """
        n = len(W)
        # 同时计算L_1的前驱子图
        P = []
        for i in range(n):
            P.append([])
            for v in W[i]:
                if v == inf or v == 0:
                    P[i].append(None)
                else:
                    P[i].append(i)

        L_1 = deepcopy(W)
        L_m = L_1
        for m in range(2, n):    # 分别计算m=2,...,n-1的L矩阵
            L_m, P = cls.extend_shortest_paths(L_m, W, P)
        return L_m, P
    
    @classmethod
    def faster_pairs_shortest_paths(cls, W):
        """较快的计算版本
        
        extend_shortest_paths方法的运算非常类似矩阵乘积的 :math:`O(n^3)`形式算法：
        .. math:: 
            L^{(1)} &= W
            L^{(2)} &= L^{(1)} \cdot W = W \cdot W
            L^{(3)} &= L^{(2)} \cdot W = W^2 \cdot W
            L^{(4)} &= L^{(2)} \cdot L^{(2)} = W^2 \cdot W^2
            L^{(8)} &= L^{(4)} \cdot L^{(4)} = W^4 \cdot W^4
        
        且注意当 :math:`m\ge n-1`时：:math:`L^{(m)} = L^{(n-1)}`
        
        所以借助这样的关系式，可以使用重复平方的方法进行运算，使得运算时间复杂度从 :math:`O(n^4)`变为 :math:`O(n^3\lg n)`
        
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
            >>> L_m = GeneralPairsShortestPaths.faster_pairs_shortest_paths(the_graph)
            >>> pprint(L_m)
            [[0, 1, -3, 2, -4],
             [3, 0, -4, 1, -1],
             [7, 4, 0, 5, 3],
             [2, -1, -5, 0, -2],
             [8, 5, 1, 6, 0]]
        """
        n = len(W)
        L_m = deepcopy(W)
        m = 1
        while m < n-1:
            L_m, _ = cls.extend_shortest_paths(L_m, L_m)
            m = 2*m
        return L_m


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    