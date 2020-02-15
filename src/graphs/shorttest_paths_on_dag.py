#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from ssp_basics import AbstracteSingleSourcePaths as SSP
from topological_sort import topological_sort


the_dag = {
    "r": [("s", 5), ("t", 3)],
    "s": [("t", 2), ("x", 6)],
    "t": [("x", 7), ("y", 4), ("z", 2)],
    "x": [("y", -1), ("z", 1)],
    "y": [("z", -2)],
    "z": []
}

the_dag_wthout_weights = {
    "r": ["s", "t"],
    "s": ["t", "x"],
    "t": ["x", "y", "z"],
    "x": ["y", "z"],
    "y": ["z"],
    "z": []
}


class ShortestPathsOnDAG(SSP):
    """有向无环图上的最短路径
    
    这里由于已经要求给定图是有向无环图，所以本算法等于是对`BellmanFordSSP`的特殊情况做的修改，以提高运行效率。
    
    相比bellman-ford算法，由于已经要求给定图是有向无环图，因此无需对图中的边进行|V|-1次松弛操作，而是利用对DAG的拓扑排序序列，依次取出每一条边，然后进行1次松弛操作即可
    
    Example:
        >>> dag_ssp = ShortestPathsOnDAG(the_dag, "s")
        >>> dag_ssp.show()
        s -> t, weights:  2
        s -> x, weights:  6
        s -> x -> y, weights:  5
        s -> x -> y -> z, weights:  3
    """
    
    def compute(self):
        """计算SSP
        """
        # 使用已经生成的无权重的图进行拓扑排序，因为之前的dfs实现暂不支持带权重的图结构
        # 注意：这里为了简便，帮助理解，直接使用了全局变量the_dag_wthout_weight
        topo_sequence = topological_sort(the_dag_wthout_weights)
        for u in topo_sequence:
            for v, w_uv in self.graph[u]:
                self.relax(u, v, w_uv)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
