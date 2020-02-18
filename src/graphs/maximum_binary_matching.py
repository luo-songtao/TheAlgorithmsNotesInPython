#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from  flow_network_ford_fulkerson import FordFulkerson
# 二分图
the_graph = {
    "l1": ["r1"],
    "l2": ["r1", "r3"],
    "l3": ["r2", "r3", "r4"],
    "l4": ["r3"],
    "l5": ["r3"]
}


def maximum_binary_matching(binary_graph):
    """最大二分匹配
    
    在一个二分图 :math:`G=(V, E)` 中寻找最大二分匹配，也就是寻找最大匹配的基数和匹配到的边的集合 :math:`M` （:math:`M \sub E`）
    
    可以通过将二分图转变为一个流网络，并设所有边的权重都是单位权重，然后利用Ford-Fulkerson方法来计算最大流从而实现二分图的最大匹配。
    最终的到的最大流值就是最大匹配的基，并利用生成的残存网络，可以很快就找到最大匹配的边的集合 :math:`M`
    
    Example:
        >>> from pprint import pprint
        >>> pprint(the_graph)
        {'l1': ['r1'],
         'l2': ['r1', 'r3'],
         'l3': ['r2', 'r3', 'r4'],
         'l4': ['r3'],
         'l5': ['r3']}
        >>> maximum_base, matching = maximum_binary_matching(the_graph)
        >>> maximum_base
        3
        >>> matching
        [('l1', 'r1'), ('l2', 'r3'), ('l3', 'r2')]
    """
    
    source = "s"
    target = "t"
    flow_network = {
        source: [],
        target: []
    }
    
    for l in binary_graph.keys():
        flow_network[source].append((l, 1))
        flow_network[l] = []
        for r in binary_graph[l]:
            if r not in flow_network:
                flow_network[r] = [(target, 1)]
            flow_network[l].append((r, 1))
    
    ford_filkerson = FordFulkerson(flow_network, source, target)

    largest_base = ford_filkerson.max_flows
    matching = []
    for r, _ in ford_filkerson.residual_network[target]:
        matching.append(
            (ford_filkerson.residual_network[r][0][0], r)
        )
        
    return largest_base, matching


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    