#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


def dfs(graph):
    """深度优先搜索
    
    实现中不仅记录了顶点的发现顺序；还记录了顶点的探索完成顺序
    
    Returns:
        discoverd (list): 顶点的深度优先搜索顺序
        finished (list): 顶点探索完成顺序
    """
    discoverd = []
    finished = []
    for start_vertex in graph.keys():
        dfs_recusion(graph, start_vertex, discoverd, finished)
    return discoverd, finished


def dfs_recusion(graph, start_vertex, discoverd, finished):
    if start_vertex not in discoverd:
        discoverd.append(start_vertex)
        for next_vertex in graph[start_vertex]:
            if next_vertex in discoverd:
                continue
            dfs_recusion(graph, next_vertex, discoverd, finished)
        finished.append(start_vertex)

'''仅记录顶点发现顺序的版本
def dfs(graph):
    """深度优先搜索
    """
    discoverd = []    # 使用集合也可以
    for start_vertex in graph.keys():
        dfs_recusion(graph, start_vertex, discoverd)
    return discoverd

def dfs_recusion(graph, start_vertex, discoverd):
    if start_vertex not in discoverd:
        discoverd.append(start_vertex)
        for next_vertex in graph[start_vertex]:
            if next_vertex in discoverd:
                continue
            dfs_recusion(graph, next_vertex, discoverd)
'''

'''仅记录顶点发现顺序的生成器版本
def dfs(graph):
    """深度优先搜索
    """
    discoverd = []
    for start_vertex in graph.keys():
        yield from dfs_recusion(graph, start_vertex, discoverd)

def dfs_recusion(graph, start_vertex, discoverd):
    if start_vertex not in discoverd:
        discoverd.add(start_vertex)
        yield start_vertex
        for next_vertex in graph[start_vertex]:
            if next_vertex in discoverd:
                continue
            yield from dfs_recusion(graph, next_vertex, discoverd)
'''


if __name__ == '__main__':
    the_graph = {
        "s": ["z", "w"],
        "z": ["y", "w"],
        "w": ["x"],
        "y": ["x"],
        "x": ["z"],
        "t": ["v", "u"],
        "v": ["s", "w"],
        "u": ["t", "v"]
    }
    
    for v in dfs(the_graph):
        print(v, end=" ")
    print()
    