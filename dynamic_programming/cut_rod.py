#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
利益最大化：钢条切割
"""
import math

price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]    # p[i]: 长为i米的价格

def naive_recu_cut_rod(price, n):
    """
    >>> price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    >>> naive_recu_cut_rod(price, len(price)-1)
    30
    """
    if n == 0:
        return 0
    value = - math.inf
    for i in range(1, n+1):
        value = max(value, price[i] + naive_recu_cut_rod(price, n-i))
    return value

def memoized_cut_rod(price, n):
    


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()