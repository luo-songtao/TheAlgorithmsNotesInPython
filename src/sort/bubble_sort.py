#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


def bubble_sort(array):
    """冒泡排序
    
    冒泡排序算法步骤:
        - 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
        - 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
        - 针对所有的元素重复以上的步骤，除了最后一个。
        - 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    
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
        >>> bubble_sort(the_array)
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    """
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    bubble_sort(the_array)
    print(the_array)
