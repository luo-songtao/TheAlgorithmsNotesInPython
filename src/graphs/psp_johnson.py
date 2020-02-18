#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from copy import deepcopy
from ssp_bellman_ford import BellmanFordSSP as BellmanFord
from ssp_dijkstra import DijkstraSSP as Dijkstra


the_graph = {
    "a": [("b", 3), ("c", 8), ("e", -4)],
    "b": [("d", 1), ("e", 7)],
    "c": [("b", 4)],
    "d": [("a", 2), ("c", -5)],
    "e": [("d", 6)]
}


def johnson(the_graph, v_s="s"):
    """结点对最短路径Johnson算法
    
    Johnson算法寻找结点对主要是借助了Bellman-Ford算法和Dijkstra算法特征和优势实现的，这样能使得在大型稀疏图上的其性能比Floyd-Warrshall算法表示要好。
    
    Johnson算法的主要思想是，先借助Bellman-Ford算法对给定有向图(权重可为负数，但同样不能右权重为负值的环)的所有边，进行权重调整，使得：
    第一：调整后，每个结点对之间的最短路径保持不变；第二，每条边的权重都调整为了正值。为满足这样的形式，有以下公式：
    
    .. math::

        \widehat{\omega}_{uv} = \omega_{uv} + h(u) + h(v)
        
    其中 :math:`\widehat{\omega}_{uv}` 表示调整后的权重， :math:`h` 表示一个将结点映射到实数的函数。
    
    经过调整后，权重值为正数，然后对每个结点使用Dijkstra算法来求得所有结点对的最短路径。

    可见，Johnson算法理论上运行时间，主要和Dijkstra算法中的优先队列的实现方式相关，算法中总共对Dijkstra算法调用了V次，因此Johnson算法只要在Dijkstra算法中的优先队列实现
    性能较好情况下，Johnson算法的运行时间是比Floyd-Warrshall算法的 :math:`O(n^3)` 要好的
    
    Example:
        >>> from pprint import pprint
        >>> pprint(the_graph)
        {'a': [('b', 3), ('c', 8), ('e', -4)],
         'b': [('d', 1), ('e', 7)],
         'c': [('b', 4)],
         'd': [('a', 2), ('c', -5)],
         'e': [('d', 6)]}
        >>> shortest_paths_graph = johnson(the_graph)
        >>> pprint(shortest_paths_graph)
        {'a': [('b', 1), ('c', -3), ('d', 2), ('e', -4)],
         'b': [('a', 3), ('c', -4), ('d', 1), ('e', -1)],
         'c': [('a', 7), ('b', 4), ('d', 5), ('e', 3)],
         'd': [('a', 2), ('b', -1), ('c', -5), ('e', -2)],
         'e': [('a', 8), ('b', 5), ('c', 1), ('d', 6)]}
    """
    the_graph_added_s = deepcopy(the_graph)
    the_graph_added_s[v_s] = []
    for v in the_graph.keys():
        the_graph_added_s[v_s].append((v, 0))

    bellman_ford = BellmanFord(the_graph_added_s, v_s)
    if bellman_ford.isexists_ssp is False:
        raise Exception("The input graph contains a negative-weight cycle")
    else:
        updated_weight_graph = {}
        for u in the_graph.keys():
            updated_weight_graph[u] = []
            for v, w_uv in the_graph[u]:
                h_u = bellman_ford.get_shortest_weight(u)
                h_v = bellman_ford.get_shortest_weight(v)
                updated_w_uv = w_uv + h_u - h_v
                updated_weight_graph[u].append((v, updated_w_uv))
        
        shortest_paths_graph = {}
        for u in updated_weight_graph.keys():
            dijkstra = Dijkstra(updated_weight_graph, u)
            shortest_paths_graph[u] = []
            for v in updated_weight_graph.keys():
                if u==v:
                    continue
                min_w_uv = dijkstra.get_shortest_weight(v)
                h_u = bellman_ford.get_shortest_weight(u)
                h_v = bellman_ford.get_shortest_weight(v)
                shortest_paths_graph[u].append((v, min_w_uv + h_v - h_u))
        return shortest_paths_graph
                

if __name__ == '__main__':
    import doctest
    doctest.testmod()