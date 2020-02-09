#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


import math


def shell_sort(array):
    """希尔排序
    
    希尔排序是直接插入排序的改进版。它与直接插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
    
    算法思想：将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序
    
    希尔排序实现步骤：
        - 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1
        - 按增量序列个数k，对序列进行k 趟排序
        - 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度
    
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n^2)`
            - 平均：:math:`O(n^{1.3})`
            - 最好：:math:`O(n)`
        - 空间复杂度：:math:`O(1)`
        - 稳定性：不稳定
    
    Arguments:
        array (list): 待排序数组，将在原始数组上排序
    
    Returns:
        None
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> shell_sort(the_array)
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    
    """
    seq_count = int(math.log2(len(array)))
    for seq_number in range(1, seq_count+1):
        gap = 2 ** seq_number - 1    # 增量序列的间隔，···7、3、1
        for start_index in range(len(array)):    # 增量序列的起始下标
            """对增量序列进行插入排序"""
            for index in range(start_index+gap, len(array), gap):    # 增量序列的第2，3···个数的下标
                current = array[index]
                k = 1    # 增量序列中，位于index前的第k个
                while index-k*gap >= start_index and array[index-k*gap] > current:
                    array[index] = array[index-k*gap]
                    k += 1
                array[index-(k-1)*gap] = current


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    shell_sort(the_array)
    print(the_array)
