#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com

the_graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def bfs(graph, source, target):
    """广度优先搜索
    
    Example:
        >>> from pprint import pprint
        >>> pprint(the_graph)
        {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
        >>> source = "A"
        >>> target = "F"
        >>> bfs(the_graph, source, target)
        ['A', 'C', 'F']
    """
    paths_info = {source: None}
    discoverd = {source}
    queue = [source]
    queue_size = 1
    while queue_size != 0:
        vertex = queue.pop(0)
        queue_size -= 1
        for next_vert in graph[vertex]:
            if next_vert == target:
                paths_info[next_vert] = vertex
                queue_size = 0
                break
            if next_vert not in discoverd:
                discoverd.add(next_vert)
                queue.append(next_vert)
                queue_size += 1
                paths_info[next_vert] = vertex
        
    path = []
    while True:
        pre = paths_info[target]
        path.insert(0, target)
        if pre == None:
            break
        target = pre
    return path


if __name__ == '__main__':
    import doctest
    doctest.testmod()
