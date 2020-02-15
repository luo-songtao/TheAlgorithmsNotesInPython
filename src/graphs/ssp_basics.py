#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import math


class AbstracteSingleSourcePaths:
    """单源最短路径算法抽象类
    
    注意：不能直接初始化进行使用，需要继承后，重写compute方法进行使用
    """
    
    def __init__(self, graph, source):
        """
        Args:
            graph: 有向图
            source: 源顶点
        """
        self.graph = graph
        self.source = source
        self.vertex_info = {}    # 记录每个顶点在计算ssp过程中的信息
        self.initialize_single_source()
        self.isexists_ssp = False
        self.compute()
    
    def initialize_single_source(self):
        """初始化单源路径图顶点信息
        """
        for vertex in self.graph.keys():
            self.vertex_info[vertex] = {
                "distance": math.inf,    # 记录source顶点到当前顶点的距离，默认是无穷大
                "prev": None    # 记录当前顶点在ssp中的前驱顶点
            }
        self.vertex_info[self.source]["distance"] = 0    # 将源顶点的距离归为0
    
    def relax(self, u, v, w_uv):
        """对边`u->v`进行松弛处理
        
        如果（源顶点s到后向顶点v的距离）大于（源顶点s到其前驱顶点u的距离+边`u->v`的权重），则需要对源顶点s到后向顶点v的距离进行一次更新
        """
        if self.vertex_info[v]["distance"] > self.vertex_info[u]["distance"] + w_uv:
            self.vertex_info[v]["distance"] = self.vertex_info[u]["distance"] + w_uv
            self.vertex_info[v]["prev"] = u
    
    def generate_ssp(self, t):
        """根据已经构建的SSP信息(`vertex_info`)，生成每一条路径
        """
        if self.vertex_info[t]["prev"] != None:
            if self.vertex_info[t]["prev"] != self.source:
                yield from self.generate_ssp(self.vertex_info[t]["prev"])
            yield t
    
    def show(self):
        """打印每一条SSP
        """
        for v in self.graph.keys():
            if self.vertex_info[v]["prev"] != None:
                print(self.source+" ->", " -> ".join(self.generate_ssp(v)), end=", ")
                print("weights: ", self.vertex_info[v]["distance"])

    def compute(self):
        """计算SSP
        
        该方法需要被重写
        """
        raise NotImplementedError

    