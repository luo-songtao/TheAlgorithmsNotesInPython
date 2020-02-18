#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


def insertion_sort(array):
    """直接插入排序
    
    直接插入排序基本思想是：把待排序的数据按其值的大小逐个插入到一个已经排好序的有序序列中，直到所有的数据插入完为止，得到一个新的有序序列
    
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n^2)`
            - 平均：:math:`O(n^2)`
            - 最好：:math:`O(n)`
        - 空间复杂度：:math:`O(1)`
        - 稳定性：稳定
    
    Arguments:
        array (list): 待排序数组，将在原始数组上排序
    
    Returns:
        None
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> insertion_sort(the_array)
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    """
    for i in range(1, len(array)):
        current = array[i]
        k = 1
        while i-k >= 0 and array[i-k] > current:
            array[i-k+1] = array[i-k]
            k += 1
        array[i-k+1] = current


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    insertion_sort(the_array)
    print(the_array)
