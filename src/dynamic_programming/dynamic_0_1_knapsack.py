#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
"""
Author: luo-songtao
0-1背包问题
"""


def dynamic_0_1_knapsack(items, weight):
    """
    (i,w): i-物品个数；w-背包重量
    values[i][w]存储i个物品对于背包大小w的最大价值
    """
    m = weight + 1
    n = len(items) + 1
    
    values = [[0]*m for i in range(n)]
    
    for i in range(1, n):    # 依次将第1、2、3...、n个物品放入重量为1、2、3...weight的背包中，并记录最大价值
        for w in range(1, m):
            v_i = items[i-1][0]    # 第i个物品的价值
            w_i = items[i-1][1]    # 第i个物品的重量
            if w_i <= w:
                if v_i + values[i-1][w-w_i] > values[i-1][w]:    # 如果将第i个物品放入重量上限是w的背包后，价值大于i-1个物品放入其中的价值高
                    values[i][w] = v_i + values[i-1][w-w_i]    # 放入后，存储这时的价值
                else:
                    values[i][w] = values[i-1][w]    # 否则说明第i个物品没有放入，所以价值不变
            else:
                values[i][w] = values[i-1][w]
    return values


if __name__ == "__main__":
    items = [(20,3), (40, 5), (10, 1), (15, 4), (50, 5), (25, 3)]
    values = dynamic_0_1_knapsack(items, 20)
    from pprint import pprint
    pprint(values)
