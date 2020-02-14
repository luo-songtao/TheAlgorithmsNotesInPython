#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from queue import PriorityQueue


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


class Kruskal:
    """最小生成树的Kruskal算法
    
    Kruskal算法的思想是每次添加的边都是图中权重最小的边(贪心策略)，因此这样可能会在生成过程中出现多颗子树(不相连),我们称为森林。因此需要直到所有的子树连接为一颗树，且覆盖完图中所有的节点，则代表树生成结束
    """
    
    def __init__(self, graph):
        self.graph = graph
        self.minmum_weight, self.edges = self.create()

    def create(self):
        vertexs_already_in_tree = set()
        queue = PriorityQueue()
        disjoin_set = DisjoinSet()
        for v in self.graph.keys():
            disjoin_set.make(v)
        
        for i in self.graph.keys():
            for j,w in self.graph[i]:
                queue.put((w, (i,j)))
        
        total_weight = 0
        while not queue.empty():
            w, edge = queue.get()
            if disjoin_set.find_set(edge[0]) != disjoin_set.find_set(edge[1]):
                vertexs_already_in_tree.update(edge)
                disjoin_set.union(edge[0], edge[1])
                total_weight += w
        return total_weight, vertexs_already_in_tree
        
        
if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../high_level_data_structures/'))
    
    from disjoin_set import DisjoinSet
    
    kruskal = Kruskal(connected_undirected_graph)
    print(kruskal.minmum_weight)
    print(kruskal.edges)
    