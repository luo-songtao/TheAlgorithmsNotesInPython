#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import math

from ssp_basics import AbstracteSingleSourcePaths as SSP


the_graph = {
    "s": [("t", 6), ("y", 7)],
    "t": [("x", 5), ("y", 8), ("z", -4)],
    "x": [("t", -2)],
    "y": [("x", -3), ("z", 9)],
    "z": [("s", 2), ("x", 7)]
}


class BellmanFordSSP(SSP):
    """单源最短路径的BellmanFord算法
    
    BellmanFord算法可以解决一般情况下的单源最短路径(后面简称SSP)问题，边的权重值可以为负值。
    
    BellmanFord算法运行时间为: :math:`O(VE)`
    
    Example:
        >>> from pprint import pprint
        >>> pprint(the_graph)
        {'s': [('t', 6), ('y', 7)],
         't': [('x', 5), ('y', 8), ('z', -4)],
         'x': [('t', -2)],
         'y': [('x', -3), ('z', 9)],
         'z': [('s', 2), ('x', 7)]}
        >>> bellman_ford_ssp = BellmanFordSSP(the_graph, "s")
        >>> bellman_ford_ssp.isexists_ssp
        True
        >>> bellman_ford_ssp.show()
        s -> y -> x -> t, weights:  2
        s -> y -> x, weights:  4
        s -> y, weights:  7
        s -> y -> x -> t -> z, weights:  -2
    """
    
    def compute(self):
        """计算SSP
        
        计算过程中:
            1. 对图中的每一条边 进行 :math:`\\vert V \\vert - 1` 次松弛操作，( :math:`\\vert V \\vert` 表示图的顶点数)
            2. 对每一条边进行判断，检测是否存在SSP，因为当给定的图是一个具有负值环路的图时，是不存在SSP的。如果存在，属性isexists_ssp值将为True
        """
        # 对图中的每一条边 进行 |V|-1次松弛操作，(|V|表示图的顶点数)
        for i in range(len(self.graph) - 1):
            for u in self.graph.keys():
                for v, w_uv in self.graph[u]:
                    self.relax(u, v, w_uv)
        # 判断是否存在SSP(当给定的图是一个具有负值环路的图时，是不存在SSP的)
        for u in self.graph.keys():
            for v, w_uv in self.graph[u]:
                if self.vertex_info[v]["distance"] > self.vertex_info[u]["distance"] + w_uv:
                    self.isexists_ssp = False
                    return
        self.isexists_ssp = True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    