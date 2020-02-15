#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import os
import sys
sys.path.insert(0, "../")

import math

from data_structures.queues.dynamic_priority_queue import DynamicPriorityQueue
from ssp_basics import AbstracteSingleSourcePaths as SSP


the_graph = {
    "s": [("t", 10), ("y", 5)],
    "t": [("x", 1), ("y", 2)],
    "x": [("z", 4)],
    "y": [("t", 3), ("x", 9), ("z", 2)],
    "z": [("s", 7), ("x", 6)]
}


class DijkstraSSP(SSP):
    """单源最短路径Dijkstra算法
    
    Dijkstra算法可解决有向图上的单源最短路径问题，但是它要求所有边的权重都必须是正值
    
    Example:
        >>> dijkstra_ssp = DijkstraSSP(the_graph, "s")
        >>> dijkstra_ssp.show()
        s -> y -> t, weights:  8
        s -> y -> t -> x, weights:  9
        s -> y, weights:  5
        s -> y -> z, weights:  7
    """
    
    def compute(self):
        """Dijkstra算法核心逻辑
        
        Dijkstra算法在运行过程中将图的顶点集合V分为了两部分，一部分是已经计算出最短路径的顶点，这里称为集合S，一部分是还没有计算处最短路径的顶点，即集合V-S。
        
        Dijkstra算法总是选择集合V-S中最近的节点来加入到集合S中(贪心策略)，主循环次数是图的顶点集合数，第一次迭代中进行计算的顶点u是源节点
        
        由于每轮迭代，V-S中的节点的距离值都可能发生变化，是在动态发生变化，也就意味着需要在每次提取新的最小值时，重新去排序
        
        实际上可以看到，在`DynamicPriorityQueue`的实现中，`get`方法如果传入`resort=True`，则表示在每次获取最小值的时候，会计算队列中每个元素的权重，然后进行比较。
        
        而整个算法的性能表现也是在这个优先队列的实现上。这里单独封了一个`DynamicPriorityQueue`，不是必须的，仅是为了简化这里的代码。
        """
        queue = DynamicPriorityQueue(without_data=False)
        for u in self.graph.keys():
            for v,_ in self.graph[u]:
                queue.put(
                    (
                        lambda info, v: info[v]["distance"], 
                        (self.vertex_info, v)
                    )
                )
 
        while not queue.empty():
            f, args = queue.get(resort=True)
            _, u = args
            for v, w_uv in self.graph[u]:
                self.relax(u, v, w_uv)
                

if __name__ == '__main__':
    import doctest
    doctest.testmod()
