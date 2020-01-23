#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
利益最大化：钢条切割
"""
import math


def direct_recursion_cut_rod(price, n):
    """
    >>> price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    >>> direct_recursion_cut_rod(price, len(price)-1)
    30
    """
    if n == 0:
        return 0
    value = - math.inf
    for i in range(1, n+1):
        value = max(value, price[i] + direct_recursion_cut_rod(price, n-i))
    return value


def memoized_cut_rod_aux(price, n, memo):
    if memo[n] > 0:
        return memo[0]
    
    if n == 0:
        q = 0
    else: 
        q = - math.inf
        for i in range(1, n+1):
            q = max(q, price[i] + memoized_cut_rod_aux(price, n-i, memo))
    memo[n] = q
    return q


def memoized_cut_rod(price, n):
    """
    带备忘的自顶向下动态规划法
    >>> price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    >>> memoized_cut_rod(price, len(price)-1)
    30
    """
    memo = [-math.inf for i in range(n+1)]
    return memoized_cut_rod_aux(price, n, memo)


def buttom_up_cut_rod(price, n):
    """
    自底向上动态规划法
    >>> price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    >>> buttom_up_cut_rod(price, len(price)-1)
    30
    """

    memo = [-math.inf for i in range(n+1)]
    memo[0] = 0

    for i in range(1, n+1):
        q = -math.inf
        for j in range(1, i+1):
            q = max(q, price[j]+memo[i-j])
        memo[i] = q
    return memo[n]


def extended_buttom_up_cut_rod(price, n):
    """
    记录解决方案
    >>> price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]    # p[i]: 长为i米的价格
    >>> memo, solution = extended_buttom_up_cut_rod(price, len(price)-1)
    >>> memo
    [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
    >>> solution
    [0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10]
    """
    solution = [0 for i in range(n+1)]
    memo = [-math.inf for i in range(n+1)]
    memo[0] = 0

    for i in range(1, n+1):
        q = -math.inf
        for j in range(1, i+1):
            if q < price[j] + memo[i-j]:
                q = price[j]+memo[i-j]
                solution[i] = j
        memo[i] = q
    return memo, solution


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
