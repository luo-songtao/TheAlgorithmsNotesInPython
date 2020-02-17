#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from math import inf
from copy import deepcopy

from breadth_first_search import bfs


the_graph = {
    "s": [("v1", 16), ("v2", 13)],
    "v1": [("v3", 12)],
    "v2": [("v1", 4), ("v4", 14)],
    "v3": [("v2", 9), ("t", 20)],
    "v4": [("v3", 7), ("t", 4)],
    "t": []
}


class FordFulkerson:
    r"""最大流Ford-Fulderson方法
    
    Ford-Fulderson方法依赖于三种重要思想：
        - 残存网络: 对于给定流网络 :math:`G` 和流量 :math:`f` ，残存网络 :math:`G_f` 指由那些网络中仍然有剩余空间对流量进行调整的边构成的网络。 :math:`c_f(u,v) = c(u,v) 0 f(u,v) > 0` 
        - 增广路径: 指残存网络中一条从源节点到汇点的简单路径 :math:`p`，该路径存在一个残存容量 :math:`c_f(p) = \min \lbrace c_f(u,v): (u,v) \in p \rbrace`
        - 切割: 流网络 :math:`G=(V,E)` 的一个切割 :math:`(S, T)` 将结点集合V划分为S和T=V-S两个集合，且有两个概念：净流量 :math:`f(S,T)` 和切割容量 :math:`c(S,T)`
        
        .. math::
        
            f(S,T) &= \sum_{u\in S}\sum_{v\in T} f(u,v) - \sum_{u\in S}\sum_{v\in T} f(v,u) \\
            c(S,T) &= \sum_{u\in S}\sum_{v\in T} c(u,v)
    
    最大流最小切割定理
        设 :math:`f` 是流网络 :math:`G=(V,E)` 中的一个流，该流网络的源节点为s，汇点为t，则下面的条件等价：
            1. 流量 :math:`f` 是 :math:`G` 的一个最大流
            2. 残存网络 :math:`G_f` 不包括任何增广路径
            3. :math:`\vert f \vert = c(S,T)` 其中 :math:`(S,T)` 是一个切割
    
    Ford-Fulderson方法主要实现步骤：
        1. 初始化流网络的残存网络，也就是所有的残存边的的容量等于流网络边的原始容量
        2. 使用循环：不断寻找残存网络中的增广路径，并利用增广路径上的残存容量，对残存网络进行更新
        3. 直到无法再从残存网络中找到增广路径，那么循环终止，并输出流网络的最大流值
    
    Ford-Fulderson方法如果使用广度优先搜索方法，并将边设为单位距离进行搜索，这样的实现也被称为Edmonds-Karp算法，本实现也正是使用这样的思路实现的，其算法运行时间为 :math:`O(VE^2)`
    
    Attention:
        最大流问题中的容量通常时整数，如果是有理数，那么可以通过乘以相应系数转换为整数，但如果是无理数，那么Ford-Fulderson方法可能不会终止
    
    Example:
        >>> from pprint import pprint
        >>> pprint(the_graph)
        {'s': [('v1', 16), ('v2', 13)],
         't': [],
         'v1': [('v3', 12)],
         'v2': [('v1', 4), ('v4', 14)],
         'v3': [('v2', 9), ('t', 20)],
         'v4': [('v3', 7), ('t', 4)]}
        >>> ford_fulkerson = FordFulkerson(the_graph, "s", "t")
        >>> ford_fulkerson.max_flows
        23
        >>> pprint(ford_fulkerson.residual_network)
        {'s': [('v1', (16, 12)), ('v2', (13, 11))],
         't': [('v3', (20, 1)), ('v4', (4, 0))],
         'v1': [('s', (16, 4))],
         'v2': [('v1', (4, 0)), ('v4', (14, 11)), ('s', (13, 2))],
         'v3': [('v2', (9, 0)), ('t', (20, 19)), ('v1', (12, 0)), ('v4', (7, 0))],
         'v4': [('v2', (14, 3))]}
    """
    
    def __init__(self, the_graph,s, t):
        """
        """
        self.graph = the_graph
        self.s = s
        self.t = t
        
        self.max_flows = None
        self.residual_network = None
        self.compute()
    
    def search_augmenting_path_and_remaining_capacity_by_bfs(self, residual_network, source, target):
        """广度优先搜索
        
        利用广度优先搜索残存网络中搜索指定结点，如果找到了则生成出对应路径作为增广路径，并找出增广路径上的残存容量，并返回。
        
        如果没有找到，则返回空的路径，对应残存容量将设为0并返回
        
        Args:
            residual_network: 残存网络
            source:  源节点
            target: 汇点
        
        Returns:
            augmenting_path (list), remaining_capacity (number)
        """
        paths_info = {source: (None, inf)}
        discoverd = {source}
        queue = [source]
        queue_size = 1
        while queue_size != 0:
            vertex = queue.pop(0)
            queue_size -= 1
            for next_vert, (c_uv, f_uv) in residual_network[vertex]:
                if next_vert == target:
                    paths_info[next_vert] = (vertex, c_uv-f_uv)
                    queue_size = 0
                    break
                if next_vert not in discoverd:
                    discoverd.add(next_vert)
                    queue.append(next_vert)
                    queue_size += 1
                    paths_info[next_vert] = (vertex, c_uv-f_uv)
            
        if target not in paths_info:
            return [], 0
        
        path = []
        remaining_capacity = inf
        while True:
            pre, r_f_uv = paths_info[target]
            path.insert(0, target)
            if remaining_capacity > r_f_uv:
                remaining_capacity = r_f_uv
            if pre == None:
                break
            target = pre
        return path, remaining_capacity
    
    def compute(self):
        """计算并更新残存网络，得出最大流值
        """
        residual_network = {}
        # 初始化残存网络，边上除了存储结点外，还存储的数据为(边上总的流量限制, 已经使用了的流量)
        # 如果是反向边，那么第二个元素则表示，剩余可以向正向边增添的流量限额
        for u in self.graph.keys():
            residual_network[u] = []
            for v, c_uv in self.graph[u]:
                residual_network[u].append((v, (c_uv, 0)))
        
        while True:
            # 每次使用bfs对残存网络进行搜索，查找增广路径，以及增广路径上的最大残存容量
            augmenting_path, remaining_capacity = \
                self.search_augmenting_path_and_remaining_capacity_by_bfs(residual_network, self.s, self.t)
                
            # 当不存在增广路径时，则结束循环
            if len(augmenting_path) == 0:
                break
            
            # 如果找到了增广路径，那么新找到的增广路径对残存网络进行更新
            for i in range(len(augmenting_path)-1):
                u = augmenting_path[i]
                v = augmenting_path[i+1]
                forward_edge_index = 0    # 路径上边(u,v)所在的索引位置
                for j in range(len(residual_network[u])):
                    if residual_network[u][j][0] == v:
                        forward_edge_index = j
                        break
                c_uv = residual_network[u][forward_edge_index][1][0]
                
                backward_edge_index = 0    # 路径上边(v,u)所在的索引位置
                for k in range(len(residual_network[v])):
                    if residual_network[v][k][0] == u:
                        backward_edge_index = k
                        break
                else:    # 反向边有可能不存在，因此若不存在，则对其进行初始化
                    residual_network[v].append((u, (c_uv, c_uv)))    # 反向边默认可以返回的流量正好等于边(u,v)的容量限制
                    backward_edge_index = len(residual_network[v])-1
                
                f_uv = residual_network[u][forward_edge_index][1][1] + remaining_capacity
                f_vu = residual_network[v][backward_edge_index][1][1] - remaining_capacity
                if f_uv == c_uv:
                    # 当原网络中边(u,v)没有剩余流量了，那么残存网络中就只剩下反向边(v,u)了
                    residual_network[u].pop(j)
                    residual_network[v][backward_edge_index] = (u, (c_uv, 0))
                else:
                    residual_network[u][forward_edge_index] = (v, (c_uv, f_uv))
                    residual_network[v][backward_edge_index] = (u, (c_uv, f_vu))
        
        # 计算最大流的值
        max_flows = 0
        for v in residual_network[self.s]:
            max_flows += v[1][1]
        
        self.max_flows = max_flows
        self.residual_network = residual_network

                    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
