#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


import math


def binary_merge_sort(array: list, start: int, stop: int):
    """二路归并排序
    
    主要思想：归并排序采用分治策略。将已有序的子序列合并，得到完全有序的序列。即先使每个子序列有序，再使子序列段间有序。
    
    二路归并排序也就是分为两段有序表(左右表)：
        - 把长度为n的输入序列分成两个长度为n/2的子序列
        - 对这两个子序列分别采用归并排序
        - 将两个排序好的子序列合并成一个最终的排序序列
    
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n\lg n)`
            - 平均：:math:`O(n\lg n)`
            - 最好：:math:`O(n\lg n)`
        - 空间复杂度：:math:`O(n)`
        - 稳定性：稳定
        
    Args:
        array (list): 待排序数据
        start (int): 当前处理的子序列的起始索引
        stop (int): 当前处理的子序列的结束索引(含本身)
    
    Returns:
        None
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> binary_merge_sort(the_array, 0, len(the_array) - 1)
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    
    """
    if start < stop:
        mid = (start + stop) // 2
        binary_merge_sort(array, start, mid)
        binary_merge_sort(array, mid+1, stop)
        merge(array, start, mid, stop)


def merge(array: list, start: int, mid: int, stop: int):
    """合并左右数组
    
    将array[start...mid]的有序左子序列与array[mid+1...stop]的有序右子序列合并
    
    实现步骤：
        - 分别截取出左右子序列，并在左右子序列尾加入一个值为无穷大的哨兵元素
        - 分别在左右子序列的首元素开始设置一个游标
        - 遍历i=stop-start+1次，依次比较左右子序列的当前游标位置的数，将较小处的值放置在array[i]位置处，同时将对应子序列的游标+1
        - 结束后array[start...stop]的元素也就变为有序序列了
    
    Args:
        array (list): 待排序数据
        start (int): 当前处理的子序列的起始索引
        mid (int): 左右子序列分割点索引。(mid属于左序列)
        stop (int): 当前处理的子序列的结束索引(含本身)
    
    Returns:
        None
    
    """
    left = array[start:mid+1]
    right = array[mid+1:stop+1]

    sentry = math.inf
    left.append(sentry)
    right.append(sentry)

    left_cursor, right_cursor = 0, 0

    for i in range(start, stop+1):
        if left[left_cursor] <= right[right_cursor]:
            array[i] = left[left_cursor]
            left_cursor += 1
        else:
            array[i] = right[right_cursor]
            right_cursor += 1


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 4]
    binary_merge_sort(the_array, 0, len(the_array) - 1)
    print(the_array)