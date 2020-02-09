#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


def count_sort(array, k):
    """计数排序
    
    计数排序是一个非基于比较的排序算法。其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
    
    计数排序算法运行步骤：
        - 找出待排序的数组中最大和最小的元素；
        - 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
        - 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
        - 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。
    
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n+k)`
            - 平均：:math:`O(n+k)`
            - 最好：:math:`O(n+k)`
        - 空间复杂度：:math:`O(n+k)`
        - 稳定性：稳定
    
    Args:
        array (list): 待排序数组
        k (int): 数组中元素的上界(整数)
    
    Returns:
        list: 新创建的已排序数组
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> count_sort(the_array, max(the_array))
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    """
    count_array = [0 for i in range(k+1)]
    result_array = [0 for i in range(len(array))]

    # 计数
    for i in range(len(array)):
        count_array[array[i]] += 1

    # 统计
    for i in range(1, k+1):
        count_array[i] += count_array[i-1]

    for j in range(len(array)-1, -1, -1):
        result_array[count_array[array[j]]-1] = array[j]
        count_array[array[j]] -= 1

    return result_array


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    result = count_sort(the_array, max(the_array))
    print(result)