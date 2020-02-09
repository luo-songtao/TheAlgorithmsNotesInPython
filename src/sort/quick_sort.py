#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com



import random


def quick_sort(array, start, stop):
    """快速排序
    
    快速排序使用分治法策略来把一个序列分为较小和较大的2个子序列，然后递归地排序两个子序列。
    
    快速排序实现步骤：
        - 挑选基准值：从数列中挑出一个元素，称为“基准”（pivot）
        - 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成
        - 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
    
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n^2)`    (n(n-1)(n-2)···2)
            - 平均：:math:`O(n\lg n)`
            - 最好：:math:`O(n\lg n)`
        - 空间复杂度：:math:`O(\lg n)`、最坏为 :math:`O(n)`
        - 稳定性：不稳定
    
    Arguments:
        array (list): 待排序数组，将在原始数组上排序
        start (int): 当前处理的子序列的起始索引
        stop (int): 当前处理的子序列的结束索引(含本身)
    
    Returns:
        None
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> quick_sort(the_array, 0, len(the_array)-1)
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    
    """

    while start < stop:
        bound = random_partition(array, start, stop)
        quick_sort(array, start, bound-1)
        start = bound + 1

def random_partition(array, start, stop):
    """随机分割序列
    
    从序列随机选取基准值，并将其与数组最后的值交换，然后使用partition方法进行比较并返回划分边界
    
    Arguments:
        array (list): 待排序数组，将在原始数组上排序
        start (int): 当前处理的子序列的起始索引
        stop (int): 当前处理的子序列的结束索引(含本身)
    
    returns:
        bound (int): 子序列的划分边界
    
    """
    pivot_index = random.randrange(start, stop)
    array[stop], array[pivot_index] = array[pivot_index], array[stop]
    return partition(array, start, stop)

def partition(array, start, stop):
    """划分数组
    
    实现步骤：
        - 将数组最后一个元素作为基准值进行比较
        - 设置第一个交换位置的游标是start，然后遍历i=start...(stop-1)的数依次与基准值比较，然后将比基准值小的数交换到当前的交换位置游标处，然后将游标+1
        - 在完成所有比较后，将基准值交换到当前的交换位置游标处，这时基准值左边的数都是比它小的，右边都是比它大的数
        - 最后返回此时基准值的索引作为划分子序列的边界
        
    时间复杂度：:math:`O(n)`
    
    Arguments:
        array (list): 待排序数组，将在原始数组上排序
        start (int): 当前处理的子序列的起始索引
        stop (int): 当前处理的子序列的结束索引(含本身)
    
    returns:
        bound (int): 子序列的划分边界
    
    """
    pivot = array[stop]
    cursor = start
    for i in range(start, stop):
        if array[i] <= pivot:
            array[i], array[cursor] = array[cursor], array[i]
            cursor += 1
    array[cursor], array[stop] = array[stop], array[cursor]
    return cursor


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    quick_sort(the_array, 0, len(the_array)-1)
    print(the_array)