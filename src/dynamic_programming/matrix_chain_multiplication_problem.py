#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
"""
Author: luo-songtao
矩阵链乘
"""
import math


def direct_recursion(matrix_chain_dims):
    """
    直接递归形式
    >>> matrix_chain_dims = [(30,35), (35, 15), (15, 5), (5,10), (10, 20), (20, 25)]
    >>> direct_recursion(matrix_chain_dims)
    15125
    """
    
    if len(matrix_chain_dims) <= 1:
        return 0
    elif len(matrix_chain_dims) == 2:
        return matrix_chain_dims[0][0] * matrix_chain_dims[0][1] * matrix_chain_dims[1][1]
    else:
        cost = math.inf
        for k in range(0, len(matrix_chain_dims)-1):
            the_cost = direct_recursion(matrix_chain_dims[:k+1]) + \
                       direct_recursion(matrix_chain_dims[k+1:]) + \
                        matrix_chain_dims[0][0] * matrix_chain_dims[k][1] * matrix_chain_dims[-1][1]
            cost = min(cost, the_cost)
        return cost


def up_buttom_dynamic_programming(matrix_chain_dims):
    """
    自顶向下的动态规划
    >>> matrix_chain_dims = [(30,35), (35, 15), (15, 5), (5,10), (10, 20), (20, 25)]
    >>> up_buttom_dynamic_programming(matrix_chain_dims)
    15125
    """
    
    def dp_recursion(matrix_chain_dims, i, j, costs):
        if i == j   :
            return 0
        if j - i == 1:
            return matrix_chain_dims[i][0] * matrix_chain_dims[i][1] * matrix_chain_dims[j][1]
        else:
            cost = math.inf
            for k in range(i, j):
                if (i, k) not in costs.keys():
                    cost_ik = dp_recursion(matrix_chain_dims, i, k, costs)
                    costs[(i, k)] = cost_ik
                else:
                    cost_ik = costs[(i, k)]

                if (k+1, j) not in costs.keys():
                    cost_kj = dp_recursion(matrix_chain_dims, k+1, j, costs)
                    costs[(k+1, j)] = cost_kj
                else:
                    cost_kj = costs[(k+1, j)]
                    
                the_cost = cost_ik + cost_kj + matrix_chain_dims[i][0] * matrix_chain_dims[k][1] * matrix_chain_dims[j][1]
                cost = min(cost, the_cost)
            costs[(i,j)] = cost
            return cost
    
    costs = {}
    return dp_recursion(matrix_chain_dims, 0, len(matrix_chain_dims)-1, costs)
    

def buttom_up_dynamic_programming(matrix_chain_dims):
    """
    自底向上
    >>> matrix_chain_dims = [(30,35), (35, 15), (15, 5), (5,10), (10, 20), (20, 25)]
    >>> buttom_up_dynamic_programming(matrix_chain_dims)
    15125
    """
    
    costs = {}
    for x  in range(len(matrix_chain_dims)):
        costs[(x,x)] = 0
    for gap in range(1, len(matrix_chain_dims)):    # 分批计算出间隔为1，2，3...n-1的
        for i in range(len(matrix_chain_dims)-gap):
            j = i + gap
            cost = math.inf
            for k in range(i, j):
                the_cost = costs[(i,k)] + costs[(k+1,j)] + matrix_chain_dims[i][0] * matrix_chain_dims[k][1] * matrix_chain_dims[j][1]
                cost = min(cost, the_cost)
            costs[(i,j)] = cost
    return costs[(0,len(matrix_chain_dims)-1)]


def buttom_up_dynamic_programming2(matrix_chain_dims):
    """
    自底向上
    >>> matrix_chain_dims = [(30,35), (35, 15), (15, 5), (5,10), (10, 20), (20, 25)]
    >>> c, s = buttom_up_dynamic_programming2(matrix_chain_dims)
    >>> c[(0,5)]
    15125
    >>> s[(0,5)]    # means (0,2)、(3,5)
    2
    """
    
    costs = {}
    solution = {}
    for x  in range(len(matrix_chain_dims)):
        costs[(x,x)] = 0
    for gap in range(1, len(matrix_chain_dims)):    # 分批计算出间隔为1，2，3...n-1的
        for i in range(len(matrix_chain_dims)-gap):
            j = i + gap
            the_cost = math.inf
            the_k = None
            for k in range(i, j):
                cost = costs[(i,k)] + costs[(k+1,j)] + matrix_chain_dims[i][0] * matrix_chain_dims[k][1] * matrix_chain_dims[j][1]
                if cost < the_cost:
                    the_cost = cost
                    the_k = k
            costs[(i,j)] = the_cost
            solution[(i, j)] = the_k
    return costs, solution

def print_parens(s, i,j):
    if i == j:
        print("A%d"%(i+1), end="")
    else:
        print("(", end="")
        print_(s, i, s[(i,j)])
        print_(s, s[(i,j)]+1, j)
        print(")",end="")


        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    matrix_chain_dims = [(30,35), (35, 15), (15, 5), (5,10), (10, 20), (20, 25)]
    c,s = buttom_up_dynamic_programming2(matrix_chain_dims)
    print_parens(s,0,5)
