#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


import math


def radix_sort(array, base=10):
    """基数排序
    
    基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。
    
    基数排序实现步骤：
        - 先取得数组中的最大数，并取得位数
        - array为原始数组，从最低位开始取每个位组成radix二元数组，其中每个子数组存放当前位上数相同的数字，按顺序加入
        - 按顺序合并当前radix二元数组中的所有数组成新的array，重复前一步进入下一位的处理
        - 完成所有位的处理后，array数组即是有序的
        
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n*k)`
            - 平均：:math:`O(n*k)`
            - 最好：:math:`O(n*k)`
        - 空间复杂度：:math:`O(n+k)`
        - 稳定性：稳定
    
    Arguments:
        array (list): 待排序数组
        base (int): 待排序数组元素数字的基数。默认为10进制
    
    Returns:
        None
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> radix_sort(the_array)
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]    
    
    """
    max_item = max(array)
    places = math.floor(math.log(max_item, base))    # 最大值的位数

    radix_array = [[] for i in range(base)]
    for i in range(places+1):    # 从最低位开始依次进行排序

        for item in array:    # 根据对应位的数字进行分类
            digit = (item//(base**i)) % base
            radix_array[digit].append(item)

        array.clear()
        for arr in radix_array:    # 按照位数值从低到高重新组合新的数组
            array.extend(arr)
            arr.clear()


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    radix_sort(the_array)
    print(the_array)

