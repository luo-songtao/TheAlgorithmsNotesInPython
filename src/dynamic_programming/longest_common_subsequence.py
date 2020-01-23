#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
最长公共子序列问题
"""


def lcs_length(s1, s2):
    """
    逐个遍历S1,S2所有元素：
        1. 若发现相同元素s_i=s_j，那么子序列S1[:i]和S2[:j]的lcs长度应该是子序列S1[:i-1]和S2[:j-1]的lcs长度值+1
        2. 否则S1[:i]和S2[:j]的lcs长度必定等于S1[:i-1]和S2[:j]或者S1[:i]和S2[:j-1]的lcs长度
    可见这种情形也具备
        最优子结构：S1[:10]和S2[:15]的lcs最优解包含了子问题S1[:8]和S2[:15]的lcs最优解
        重叠子问题：S1[:10]和S2[:15]和S1[:12]和S2[:18]同时包括了如S1[:8]和S2[:8]的lcs的子问题
    不过这里的动态规划问题是在根据条件排除子问题
    """
    m = len(s1)+1
    n = len(s2)+1

    count_table = [[0]*n for i in range(m)]
    record_table = [[None]*n for i in range(m)]

    for i in range(1, m):    # 将i比作纵坐标
        for j in range(1, n):    # 将j比作横坐标
            if s1[i-1] == s2[j-1]:    # 一旦发现一个有相同元素，就记录它是前一段的LCS长度的值+1
                count_table[i][j] = count_table[i-1][j-1] + 1
                record_table[i][j] = "left-up"    # 横纵坐标都减了1，所以是left-up方向
            elif count_table[i-1][j] >= count_table[i][j-1]:
                count_table[i][j] = count_table[i-1][j]
                record_table[i][j] = "up"    # 纵坐标-1，方向up
            else:
                count_table[i][j] = count_table[i][j-1]
                record_table[i][j] = "left"    # 横坐标-1，方向left
    return count_table, record_table


def print_lcs(record_table, s1, i, j):
    if i == 0 or j == 0:
        return
    if record_table[i][j] == "left":
        print_lcs(record_table, s1, i, j-1)
    elif record_table[i][j] == "up":
        print_lcs(record_table, s1, i-1, j)
    elif record_table[i][j] == "left-up":
        print_lcs(record_table, s1, i-1, j-1)
        print(s1[i-1])


if __name__ == "__main__":
    s1 = ["A", "B", "C", "B", "D", "A", "B"]
    s2 = ["B", "D", "C", "A", "B", "A"]

    c, r = lcs_length(s1, s2)
    from pprint import pprint
    pprint(c)
    pprint(r)
    print_lcs(r, s1, len(s1), len(s2))

