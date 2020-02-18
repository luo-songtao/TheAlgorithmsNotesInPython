#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from math import inf
from pprint import pprint

the_graph = {
    "s": [("v1", 16), ("v2", 13)],
    "v1": [("v3", 12)],
    "v2": [("v1", 4), ("v4", 14)],
    "v3": [("v2", 9), ("t", 20)],
    "v4": [("v3", 7), ("t", 4)],
    "t": []
}


class PushRelabel:
    r"""最大流算法-Push-Relabel算法
    
    最大流算法的最快实现都是基于Push-Relabel算法，同时它也能有效解决其他流问题，如最小成本流问题。
    
    Push-Relabel算法比Ford-Fulkerson方法局域性更强。因为它不是对整个残存网络进行检查，然后选择一条增广路径，
    而是一个结点一个结点地进行查看，每一步只检查当前结点的邻结点。且执行过程中，Push-Relabel算法并不保持流量守恒性质。
    并维持一个preflow，它是一个VxV到R的一个函数f,该函数满足以下容量限制性质。
    对于所有的 :math:`u \in V-\{ s \}`
    
    .. math:: \sum_{v\in V}f(v,u) - \sum_{v \in V}f(u,v) \ge 0
    
    也就是进入一个结点的流可以大于流出该结点的流：
    
    .. math:: e(u) = \sum_{v\in V}f(v,u) - \sum_{v \in V}f(u,v)
    
    称为进入结点u的超额流(excess flow)。一个结点的超额流是进入该结点的流超过流出该结点的流的部分。
    如果对于 :math:`u \in V-\{ s, t \}` ,有 :math:`e(u)>0` ,则称结点u溢出(overflowing)

    因此对于每一个结点 :math:`u \in V-\{ s, t \}` ：
        - 为了容纳额外的流，每个结点都有一个可以容纳超额流的地方
        - 每个结点都有一个高度，一开始默认为0，且会随着算法推进而增加。对于s和t结点，高度始终是 :math:`\vert V \vert`和0。
    
    Example:
        >>> from pprint import pprint
        >>> pprint(the_graph)
        {'s': [('v1', 16), ('v2', 13)],
         't': [],
         'v1': [('v3', 12)],
         'v2': [('v1', 4), ('v4', 14)],
         'v3': [('v2', 9), ('t', 20)],
         'v4': [('v3', 7), ('t', 4)]}
        >>> push_relabel = PushRelabel(the_graph, "s", "t")
        >>> push_relabel.max_flows
        23
        >>> pprint(push_relabel.residual_network)
        {'s': [],
         't': [('v3', (20, 1)), ('v4', (4, 0))],
         'v1': [('s', (16, 0))],
         'v2': [('s', (13, 0)), ('v1', (4, 0)), ('v4', (14, 11))],
         'v3': [('v2', (9, 0)), ('t', (20, 19)), ('v1', (12, 0)), ('v4', (7, 0))],
         'v4': [('v2', (14, 3))]}
        >>> pprint(push_relabel.vertex_info)
        {'s': {'e': -23, 'h': 6},
         't': {'e': 23, 'h': 0},
         'v1': {'e': 0, 'h': 7},
         'v2': {'e': 0, 'h': 7},
         'v3': {'e': 0, 'h': 1},
         'v4': {'e': 0, 'h': 6}}
    """

    def __init__(self, graph, s, t):
        self.graph = graph
        self.s = s
        self.t = t
        
        self.max_flows = None
        self.vertex_info = {}
        self.residual_network = {}
        self.compute()
        
    def initialize_preflow(self):
        """初始化预流
        """
        for u in self.graph.keys():
            # 将所有结点的超额流和高度都初始化为0
            self.vertex_info[u] = {
                "e": 0,
                "h": 0
            }
            if u not in self.residual_network:
                self.residual_network[u] = []
            for v, c_uv in self.graph[u]:
                if u == self.s:    
                    # 设置了预流后，等同于从源节点预先推送了与其相邻边的容量大小的流，
                    # 因此它的超流是所有与其相邻边的容量大小的流的和的相反数
                    self.vertex_info[self.s]["e"] -= c_uv
                    # 同时由于边(s,v)已经饱和，所以不能将边(s,v)加入到残存网络，但需要将其反向边加入到网络
                    # 并把反向边的流设为0，因为原始边处于饱和了
                    if v not in self.residual_network:
                        self.residual_network[v] = [(u, (c_uv, 0))]    # 反向边
                    else:
                        self.residual_network[v].append((u, (c_uv, 0)))
                else:
                    # 其余所有原始边依次加入搭配残存网络中
                    self.residual_network[u].append((v, (c_uv, 0)))
        # 将源结点高度设为结点的数|V|
        self.vertex_info[self.s]["h"] = len(self.graph)
        # 将与源结点相邻的所有结点的超额流设置为c(s,v)
        for v, c_uv in  self.graph[self.s]:
            self.vertex_info[v]["e"] = c_uv

    def push(self, the_u, the_v):
        """push flow操作
        
        该方法调用时：u处于overflowing，且残存网络中(u,v)边还有剩余容量，并且u.h = v.h + 1
        """
        delta_f = self.vertex_info[the_u]["e"]
        for v,_ in self.graph[the_u]:  
            # 如果残存边(u,v)是原始边，那么将进行正向增流  
            if the_v == v:
                for i in range(len(self.residual_network[the_u])):
                    # (u,v)必定存在，此处判断的目的只是为了确认v的位置,
                    # 并且由于已经确认了位置，那么将在最后break出这一层for循环
                    if self.residual_network[the_u][i][0] == v:
                        c_uv = self.residual_network[the_u][i][1][0]
                        if delta_f > c_uv - self.residual_network[the_u][i][1][1]:
                            delta_f = c_uv - self.residual_network[the_u][i][1][1]
                        # 对残存网络中的原始边增流
                        f_uv = self.residual_network[the_u][i][1][1] + delta_f
                        self.residual_network[the_u][i] = (v, (c_uv, f_uv))
                        
                        # 对原始边的反向边减流
                        for j in range(len(self.residual_network[the_v])):
                            b_u = self.residual_network[the_v][j][0]
                            f_vu = self.residual_network[the_v][j][1][1]
                            if b_u == the_u:    # 判断当前原始边的反向边是否在残存网络中，如果在，那么直接减流
                                self.residual_network[the_v][j] = (the_u, (c_uv, f_vu-delta_f))
                                break
                        else:    # 如果没有，那么就要添加一条，并将反向边默认的流先设为边的容量限额，再减流
                            self.residual_network[the_v].append((the_u, (c_uv, c_uv-delta_f)))
                        break
                break    # 因为已经确认当前残存边是一条原始边，因此必须break，这样后面的else代码块的代码才会跳过
        else:
            # 如果for循环中没有触发break，那么说明当前残存边是一条原始边的反向边，所以进行逆向增流
            for i in range(len(self.residual_network[the_v])):
                # (v,u)必定存在，此处判断的目的只是为了确认u的位置
                # 并且由于已经确认了位置，那么将在最后break出这一层for循环
                if self.residual_network[the_v][i][0] == the_u:
                    c_vu = self.residual_network[the_v][i][1][0]
                    if delta_f > self.residual_network[the_v][i][1][1]:
                        delta_f = self.residual_network[the_v][i][1][1]
                    
                    # 将反向边的流减少
                    f_vu = self.residual_network[the_v][i][1][1] - delta_f
                    self.residual_network[the_v][i] = (the_u, (c_vu, f_vu))
                    
                    # 将反向边的原始边的流增加
                    for j in range(len(self.residual_network[the_u])):
                        b_v = self.residual_network[the_u][j][0]
                        f_uv = self.residual_network[the_u][j][1][1]
                        if b_v == the_v:    # 判断当前反向边的原始边是否还在残存网络中，如果在，那么直接增加
                            self.residual_network[the_u][j] = (the_v, (c_vu, f_uv+delta_f))
                            break
                    else:    # 否则意味着当前反向边的原始边已经被删掉了，那么重新添加新的
                        self.residual_network[the_u].append((the_v, (c_vu, delta_f)))
                    break
        
        self.vertex_info[the_u]["e"] -= delta_f
        self.vertex_info[the_v]["e"] += delta_f
        
    def relabel(self, u):
        """relabel操作(重新调整结点高度)
        
        该方法调用时：u需要处于overflowing，且对于所有的v in V，残存网络中存在边(u,v)，且u.h <= v.h
        """
        min_h = inf
        for v,_ in self.residual_network[u]:
            if min_h > self.vertex_info[v]["h"]:
                min_h = self.vertex_info[v]["h"]
        self.vertex_info[u]["h"] = min_h + 1

    def compute(self):
        """Push-Relabel算法主逻辑
        """
        self.initialize_preflow()
        
        while True:
            for u in self.residual_network.keys():
                if u == self.s or u == self.t:
                    continue
                # 当结点超额流>0时才进行push和relabel操作
                if self.vertex_info[u]["e"] > 0:
                    for i in range(len(self.residual_network[u])):
                        v = self.residual_network[u][i][0]
                        c_uv = self.residual_network[u][i][1][0]
                        f_uv = self.residual_network[u][i][1][1]
                        # 重打标签调整高度 u
                        if self.vertex_info[u]["h"] <= self.vertex_info[v]["h"]:
                            self.relabel(u)
                        # 推流 u -> v
                        if c_uv - f_uv > 0 and self.vertex_info[u]["h"] == self.vertex_info[v]["h"] + 1:
                            self.push(u,v)
                            # 判断推流后，边(u,v)是否达到饱和状态，如果是，那么需要从残存网络删掉它
                            if self.residual_network[u][i][1][0] == self.residual_network[u][i][1][1]:
                                self.residual_network[u].pop(i)
                                break
                    break
            else:
                break
        
        self.max_flows = self.vertex_info[self.t]["e"]
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
