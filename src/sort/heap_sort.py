#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com

import math


def heap_sort(array: list):
    """堆排序
    
    堆排序步骤：
        - 对待排序数组建立二叉最大堆，得到堆顶最大元素
        - 然后堆顶元素放到堆尾，再剔除出堆，并对剩下的元素回到第一步处理，最终数组的元素就会按升序排列
    
    算法复杂度：
        - 时间复杂度:
            - 最坏：:math:`O(n\lg n)`
            - 平均：:math:`O(n\lg n)`
            - 最好：:math:`O(n\lg n)`
        - 空间复杂度：:math:`O(1)`
        - 稳定性：不稳定
    
    Args:
        array (list): 待排序数组
        
    Returns:
        None
    
    Example:
        >>> the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
        >>> heap_sort(the_array, max(the_array))
        >>> the_array
        [3, 7, 7, 8, 18, 21, 22, 27, 27, 36, 36, 41, 43, 45, 47, 79, 84]
    """
    heap = BinaryMaxHeap()
    heap.build_max_heap(array)
    heap_size = len(array)
    for i in range(len(array)-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        heap.max_heapify(array, 0, heap_size)


if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../data_structures/heaps/'))
    from binary_max_heap import BinaryMaxHeap
    
    the_array = [41,22,36,7,21,27,18,3,79,8,43,27,45,36,84,7,47]
    heap_sort(the_array)
    print(the_array)