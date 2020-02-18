#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import math


connected_undirected_graph = {
    "a": [("b", 4), ("h", 8)],
    "b": [("a", 4), ("c", 8), ("h", 11)],
    "c": [("b", 8), ("i", 2), ("f", 4), ("d", 7)],
    "d": [("c", 7), ("f", 14), ("e", 9)],
    "e": [("d", 9), ("f", 10)],
    "f": [("e", 10), ("d", 14), ("c", 4), ("g", 2)],
    "g": [("i", 6), ("h", 1), ("f", 2)],
    "h": [("a", 8), ("i", 7), ("g", 1)],
    "i": [("c", 2), ("h", 7), ("g", 6)]
}


class MinmumSpanningTree:
    """最小生成树
    
    根据连通无向图，得到最小生成树
    
    采用贪心法，创建时，每次选取权重最小的边，除了第一次选取外，其余情况下，这条最小权重的边都必须满足的其中一个顶点已经在树中，而另一个顶点却不在树中，那么然后将这条边加入到树中。最终生成的树将是一输入的连通无向图的一颗最小生成树
    
    Example:
        >>> mst = MinmumSpanningTree(connected_undirected_graph)
        >>> mst.minmum_weight    # 最小生成树的权重值
        37
        >>> mst.edges    # 最小生成树的边
        [('g', 'h'), ('f', 'g'), ('c', 'f'), ('c', 'i'), ('c', 'd'), ('a', 'h'), ('a', 'b'), ('d', 'e')]
    """
    
    def __init__(self, graph):
        """
        Args:
            graph: 连通无向图
        """
        self.graph = graph
        self.root = root
        self.n = len(graph)
        
        self.edges = []
        self.minmum_weight = None
        self.create()
    
    @property
    def vectexs(self):
        for v in self.graph.keys():
            yield v
    
    def minmum_weight_edge(self, exclude_vectexs):
        """每次选取与已生成的最小生成树连接的权重最小的边加入到树中
        
        这里的实现方式类似prim算法，但没有优化
        """
        min_w_edge = (None, None)
        min_w = math.inf
        for v in self.vectexs:
            for neighbor, weight in self.graph[v]:
                if v in exclude_vectexs and neighbor in exclude_vectexs:
                    continue
                if len(exclude_vectexs) == 0 or \
                (v in exclude_vectexs and neighbor not in exclude_vectexs) or \
                (v not in exclude_vectexs and neighbor in exclude_vectexs):
                    if weight < min_w:
                        min_w = weight
                        min_w_edge = (v, neighbor)
        return min_w_edge, min_w
    
    def create(self):
        A = set()
        total_weight = 0
        while len(A) != self.n:
            edge, weight = self.minmum_weight_edge(A)
            A.update(edge)
            total_weight += weight
            self.edges.append(edge)
        self.minmum_weight = total_weight
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()