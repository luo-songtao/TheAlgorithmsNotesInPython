#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from deep_first_search import dfs_recusion


def strongly_connected_components(graph):
    """计算强连通分量
    
    实现步骤：
        1. 对有向图graph进行一次深度优先搜索，获取到一个顶点探索完成序列finished
        2. 对有向图graph进行转置(反转边的方向)，得到转置图。
        3. 对转置图进行一次深度优先搜索，但是其预设的搜索顺序按照finished的逆序进行，并记录下该次搜索中的每一颗深度优先树的顶点，则最终得到的每一颗深度优先树的顶点集合就是graph一个强连通分量
    
    该算法能得以成功是因为，有向图与其转置图的强连通分量是相同的，但转置后强连通分量之间的方向被反过来了，因此借助这样的事实，利用上面的两次dfs，然后搜集第2次dfs得到的每一颗深度优先树的顶点就能得出所有的强连通分量
    
    Args:
        graph: 有向图
    """
    
    # 1. 对graph进行依次深度优先搜索，拿到
    discoverd = []    # 顶点的探索顺序
    finished = []    # 顶点探索完成的顺序：逆序的。第一个是最后才探索完成的
    for start_vertex in graph.keys():
        dfs_recusion(graph, start_vertex, discoverd, finished)
    # 2. 计算转置图
    graph_t = tranpose_graph(graph)
    # 3. 对graph_t进行深度优先探索，但是预设探索顺序将按照对原图的dfs的顶点探索完成序列的逆序
    discoverd.clear()
    gt_finished = []
    forests = []    # 深度优先森林
    for vertex in reversed(finished):   # 使用逆序结果
        dfs_recusion(graph_t, vertex, discoverd, gt_finished)
        # 当其实探索节点被探索完成，则意味着得到了一颗深度优先树
        if gt_finished and vertex == gt_finished[0]:
            forests.append(gt_finished[:])
            gt_finished.clear()
    return forests


def tranpose_graph(graph):
    """对图进行转置
    """
    graph_t = {}
    for i in graph.keys():
        for j in graph[i]:
            if j not in graph_t:
                graph_t[j] = []
            graph_t[j].append(i)
    return graph_t


if __name__ == '__main__':
    the_graph1 = {
        "a": ["b"],
        "b": ["c", "e", "f"],
        "c": ["d", "g"],
        "d": ["c", "h"],
        "e": ["a", "f"],
        "f": ["g"],
        "g": ["f", "h"],
        "h": ["h"],
    }
    
    the_graph2 = {
        "x": ["z"],
        "y": ["x"],
        "z": ["y", "w"],
        "w": ["x"],
        "s": ["z", "w"],
        "v": ["s", "w"],
        "t": ["u", "v"],
        "u": ["t", "v"],
    }
    
    print("the graph1's scc:")
    for i in strongly_connected_components(the_graph1):
        print(i)
    
    print("the graph2's scc:") 
    for i in strongly_connected_components(the_graph2):
        print(i)