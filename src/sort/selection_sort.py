#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


def selection_sort(array):
    """直接选择排序
    
    主要思想：先标记n个元素中最小的，然后与第一个元素交换位置；然后对剩下的n-1个元素重复前一步骤，最终即可得到升序排列的结果
    
    n个元素的直接选择排序可经过n-1趟直接选择排序得到有序结果：
        - 初始状态：无序区为R[1..n]，有序区为空
        - 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为array[1..i-1]和array[i..n]
        - n-1趟后，数组便是有序的了
    
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n^2)`
            - 平均：:math:`O(n^2)`
            - 最好：:math:`O(n^2)`
        - 空间复杂度：:math:`O(1)`
        - 稳定性：不稳定
    
    Arguments:
        array (list): 待排序数组，将在原始数组上排序
    
    Returns:
        None
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> selection_sort(the_array)
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    
    """
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != i:
            array[min_index], array[i] = array[i], array[min_index]


def selection_sort2(array):
    """直接选择排序2
    
    第二种直接选择排序与第一种实现方式原理相同，只不过第二种方式是同时寻找最小最大元素
    
    """
    for i in range(len(array)//2+1):
        min_index = i
        max_index= len(array) - 1 - i
        if array[min_index] >= array[max_index]:
            array[min_index], array[max_index] = array[max_index], array[min_index]
        
        for j in range(i+1, len(array)-i):
            if array[min_index] > array[j]:
                min_index = j
            elif array[max_index] < array[j]:
                max_index = j
        if min_index != i:
            array[min_index], array[i] = array[i], array[min_index]
        if max_index != len(array) - 1 - i:
            array[max_index], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[max_index]


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    selection_sort2(the_array)
    print(the_array)
