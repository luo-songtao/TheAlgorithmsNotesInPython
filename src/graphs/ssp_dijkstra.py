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
        >>> from pprint import pprint
        >>> pprint(the_graph)
        {'s': [('t', 10), ('y', 5)],
         't': [('x', 1), ('y', 2)],
         'x': [('z', 4)],
         'y': [('t', 3), ('x', 9), ('z', 2)],
         'z': [('s', 7), ('x', 6)]}
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
        
        由于每轮迭代，V-S中的节点的距离值都可能发生变化，是在动态发生变化。
        而Python中无法直接给优先级队列传递指针，因此这里单独封装了一个DynamicPriorityQueue，可以用于在每次获取下一个数据时，实时的计算当前队列中最小的值并返回。
        只要调用queue.get方法时传入rebuild=True参数，但是这样会增加程序的运行时间。
        
        而整个Dijkstra算法的运行时间其实也主要是在于这个优先级队列的实现上，理论上使用最小二叉堆实现的优先级队列，运行时间为 :math:`O((V+E)\lg V)` 当边数远远大于结点数时 :math:`O(E\lg V)`.
        
        不过本实现中，使用的最小二叉堆的实现还不是最优的情况，属于待优化的情况。
        
        另外如果使用斐波那契堆( :math:`O(V\lg V + E)` )或者使用van emde boas tree ( :math:`O((V+E)\lg \lg V)` ) 实现的优先队列，可以达到更好的性能。
        
        由此可见 Dijkstra算法的性能其实主要在于使用的最小优先队列的实现上。
        """
        queue = DynamicPriorityQueue(without_data=False)
        for u in self.graph.keys():
            queue.put(
                (
                    lambda info, v: info[v]["distance"], 
                    (self.vertex_info, u)
                )
            )
        while not queue.empty():
            _, (_, u) = queue.get(rebuild=True)
            for v, w_uv in self.graph[u]:
                self.relax(u, v, w_uv)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
