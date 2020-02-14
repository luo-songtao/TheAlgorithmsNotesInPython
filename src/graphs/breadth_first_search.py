#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com

        
def bfs(graph, start_vertex):
    """广度优先搜索
    """
    discoverd = {start_vertex}
    queue = [start_vertex]
    while len(queue) != 0:
        vertex = queue.pop(0)
        for next_vert in graph[vertex]:
            if next_vert not in discoverd:
                discoverd.add(next_vert)
                queue.append(next_vert)
        yield vertex


if __name__ == '__main__':
    the_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    for v in bfs(the_graph, start_vertex):
        print(v, end="")
    print()
    
