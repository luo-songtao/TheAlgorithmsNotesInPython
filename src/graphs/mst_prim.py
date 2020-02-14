#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from queue import PriorityQueue


class Prim:
    """最小生成树Prim算法
    
    Prim算法的思想是每次添加的边总能构成一颗树(全部相连),且每次添加的边的权重总是与已生成的前驱子树相连的边中最小的(贪心策略)
    """
    
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.n = len(self.graph)
        self.minmum_weight, self.edges = self.create()
    
    def create(self):
        """构建最小生成树
        
        使用优先级队列添加新的与已生成的前驱子树相连的边。不断循环添加新的边加入的已生成的前驱子树中，直到覆盖完图中所有的顶点
        
        由于生成过程中会不断将边加入到队列中，因此该算法的时间复杂度在于优先级队列的实现方式。
        """
        queue = PriorityQueue()
        queue.put((0, (None, self.root)))
        vertexs_already_in_tree = set()    # 存储已经生成的前驱子树中的节点
        edges = {}    # 存储树结构
        total_weight = 0     # 生成树的总权重
        while 1:
            weight, vertex = queue.get()    # 每次取与前驱子树相连，且权重最小的边
            from_vertex, to_vertex = vertex
            if to_vertex in vertexs_already_in_tree:    # 如果边的顶点已经在生成的前驱子树中，那么跳过
                continue
            total_weight += weight    # 更新已生成的前驱子树的权重值
            # 记录树结构
            if from_vertex not in edges:
                edges[from_vertex] = {to_vertex}
            else:
                edges[from_vertex].add(to_vertex)
            # 记录已生成的前驱子树节点情况
            vertexs_already_in_tree.add(to_vertex)
            if len(vertexs_already_in_tree) == self.n:    # 当生成树已经覆盖所有的顶点，则生成完毕
                break
            # 遍历新的与已生成的前驱子树相连的边
            for v, w in self.graph[to_vertex]:
                if v not in vertexs_already_in_tree:
                    queue.put((w, (to_vertex, v)))
        return total_weight, edges
        

if __name__ == '__main__':
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
    
    prim = Prim(connected_undirected_graph, "c")
    print(prim.minmum_weight)
    print(prim.edges)
    