#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import os
import sys
sys.path.insert(0, "../")
from data_structures.heaps.binary_min_heap import BinaryMinHeap as BaseQueue


class DynamicPriorityQueue(BaseQueue):
    """优先队列-动态化
    
    基于二叉最小堆实现的优先级队列，同时支持一些特殊形式的权重值进行比较。这也是这里命名为`动态`的原因。
    
    动态化是指支持多种形式的权重值形式:
        - 纯权重形式: `[1,2,3,4,5,6]`
        - 一般形式(同标准库中的PriorityQueue): `[(1, "v1"), (2, "v2"), (3, "v3"), (4, "v4"), (5, "v5"), (6, "v6"), ]`
        - 函数形式: `[(function, args), (function, args), ...]`。该形式下将在每次比较时，对函数进行调用，将其返回值作为比较值，这样可以用在一些特定的需要动态更改权重值的场景下
        
    Example:
        >>> queue = DynamicPriorityQueue()
        >>> data = [9,3,5,8,7,2,6]
        >>> _ = [queue.put(i) for i in data]
        >>> queue.get()
        2
        >>> queue = DynamicPriorityQueue(without_data=False)
        >>> f = lambda x,y: x*y
        >>> data = [9,3,5,8,7,2,6]
        >>> _ = [queue.put((f,(i,j))) for i in data for j in data]
        >>> _f, args = queue.get()
        >>> _f(*args)
        4
    """
    
    def __init__(self, without_data=True):
        self.items = []
        self.without_data = without_data
    
    def put(self, item):
        self.items.insert(0, item)
        self.min_heapify(self.items, 0, len(self.items), self.without_data)
    
    def get(self, resort=False):
        if resort:
            self.build_min_heap(self.items, self.without_data)
        return self.items.pop(0)

    def empty(self):
        return True if len(self.items) == 0 else False
    
    def min_heapify(self, array: list, index: int, heap_size: int, without_data=True):
        """最小堆堆化处理，维护最小堆的性质
        
        最小堆性质：父节点必须小于等于左右子节点
        
        根据最小堆的性质将指定索引处的数调整到堆的它合适的位置:
            - 将指定index处的值x与其左右孩子的进行比较，将最小的孩子与其交换位置，以满足最小堆性质，并再次递归处理x
            - 当指定index处的值x比其左右孩子的都大，则不用再递归

        时间复杂度：:math:`O(lg n)`,n表示堆大小
        
        Args:
            array (list): 存放堆数据的数组
            index (int): 指定的索引
            heap_size (int): 当前堆有效元素个数。(array[0:heap_size-1]中存放的才是堆上有效的元素)
            without_data (bool): 如果为False，则期望每个元素应是一个二元元组，并将元组第一个元素作为值进行比较，默认为True
        """
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        
        smallest_index = index
        if without_data is False:
            if type(array[index][0]).__name__ == "function":
                if left <= heap_size-1 and array[left][0](*array[left][1]) < array[index][0](*array[index][1]):
                    smallest_index = left
                if right <= heap_size-1 and array[right][0](*array[right][1]) < array[smallest_index][0](*array[smallest_index][1]):
                    smallest_index = right
            else:
                if left <= heap_size-1 and array[left][0] < array[index][0]:
                    smallest_index = left
                if right <= heap_size-1 and array[right][0] < array[smallest_index][0]:
                    smallest_index = right
        else:
            if left <= heap_size-1 and array[left] < array[index]:
                smallest_index = left
            if right <= heap_size-1 and array[right] < array[smallest_index]:
                smallest_index = right

        if smallest_index != index:     # 如果父节点不是最小的，那么与对应最小的子节点交换位置，并继续递归判断下一级
            array[index], array[smallest_index] = array[smallest_index], array[index]
            self.min_heapify(array, smallest_index, heap_size, without_data)
        
if __name__ == '__main__':

    import doctest
    doctest.testmod()
    