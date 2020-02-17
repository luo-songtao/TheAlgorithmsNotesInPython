#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
from deep_first_search import dfs

def topological_sort(graph, start_vertex):
    """
    对图进行深度优先搜索后，顶点的探索完成顺序的逆序，就是对该graph的一种拓扑展开顺序
    """
    d, f = dfs(graph, start_vertex)
    return reversed(f)


if __name__ == '__main__':
    the_graph = {
        "内裤": ["裤子", "鞋子"],
        "裤子": ["腰带", "鞋子"],
        "衬衣": ["领带", "腰带"],
        "领带": ["夹克"],
        "腰带": ["夹克"],
        "袜子": ["鞋子"],
        "夹克": [],
        "手表": [],
        "鞋子": []
    }
    print("穿戴顺序：")
    for item in topological_sort(the_graph, "内裤"):
        print(item, "  ", end = "")
    print()