#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


def fractional_knapsack(items, weight):
    """分数背包问题
    贪心选择：按单位价值高低依次拿取直到取完所有物品或者填满背包
    """
    unit_values = [(i, round(items[i][0]/items[i][1], 4)) for i in range(len(items))]
    unit_values = sorted(unit_values, key=lambda x:x[1], reverse=True)
    
    w = 0
    values = 0
    for i, unit_value in unit_values:
        if items[i][1] <= weight - w:
            w += items[i][1]
            values += items[i][0]
            print("take 100%% item%d, values: "%(i+1), items[i][0])
        else:
            rate = (weight - w) / items[i][1]
            values += rate*items[i][0]
            print("take %0.f%% item%d, values: "%(rate*100, i+1), rate*items[i][0])
            break
    return values
    
if __name__ == '__main__':
    items = [(20,3), (40, 5), (10, 1), (15, 4), (50, 5), (25, 3)]
    values = fractional_knapsack(items, 10)
    print(values)
    
