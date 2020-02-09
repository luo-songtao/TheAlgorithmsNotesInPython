#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


def bucket_sort(array):
    """桶排序
    
    桶排序是计数排序的升级版。它假设数据是均匀分布的，并利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。
    
    桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（可能使用别的排序算法或是以递归方式继续使用桶排序进行排）。
    
    计数排序算法运行步骤：
        - 设置一个定量的数组当作空桶
        - 遍历输入数据，并且把数据一个一个放到对应的桶里去
        - 对每个不是空的桶进行排序(如使用插入排序)
        - 从不是空的桶里把排好序的数据拼接起来
    
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n^2)`
            - 平均：:math:`O(n+k)`
            - 最好：:math:`O(n)`
        - 空间复杂度：:math:`O(n+k)`
        - 稳定性：稳定
    
    Args:
        array (list): 待排序数组
    
    Returns:
        None
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> bucket_sort(the_array)
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    """

    def insertion_sort(array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
            
    max_item, min_item = max(array), min(array)
    bucket_quantity = len(array)    # 取桶数量为数组的长度
    range_mean = (max_item-min_item)/bucket_quantity    # 取级差平均值

    bucket_array = []
    for i in range(0, bucket_quantity):    # 初始化桶
        bucket_array.append([])

    for item in array:    # 将数映射到桶中，并使之满足序号大的桶中的数均大于序号小的桶中的数
        bucket_index = int((item-min_item)//range_mean)
        bucket_index = bucket_quantity - 1 if bucket_index >= bucket_quantity else bucket_index
        bucket_array[bucket_index].append(item)

    array.clear()
    for arr in bucket_array:
        insertion_sort(arr)    # 逐个排序
        array.extend(arr)


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    bucket_sort(the_array)
    print(the_array)