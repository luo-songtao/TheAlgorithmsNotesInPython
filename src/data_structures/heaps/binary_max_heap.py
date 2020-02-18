#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com


import math


class BinaryMaxHeap:
    """二叉最大堆
    
    Example:
        >>> binary_max_heap = BinaryMaxHeap()
        >>> array = [5, 2, 7, 1, 8, 10, 3]
        >>> binary_max_heap.build_max_heap(array)
        >>> binary_max_heap.extract_max(array)
        10
        >>> array2 = [(5, "i1"), (2, "i2"), (7, "i3"), (1, "i4"), (8, "i5"), (10, "i6"), (3, "i7")]
        >>> binary_max_heap.build_max_heap(array2, without_data=False)
        >>> binary_max_heap.extract_max(array2)
        (10, 'i6')
    """

    @staticmethod
    def get_parent_index(index: int):
        """计算父节点索引
        """
        return index/2 if math.fmod(index,2) == 0 else (index-1)/2

    @staticmethod
    def get_left_child_index(index: int):
        """计算左子节点索引
        """
        return 2*index

    @staticmethod
    def get_right_child_index(index: int):
        """计算右子节点索引
        """
        return 2*index + 1

    def max_heapify(self, array: list, index: int, heap_size: int, without_data=True):
        """最大堆堆化处理，维护最大堆的性质
        
        最大堆性质：父节点必须大于等于左右子节点
        
        根据最大堆的性质将指定索引处的数调整到堆的它合适的位置:
            - 将指定index处的值x与其左右孩子的进行比较，将最大的孩子与其交换位置，以满足最大堆性质，并再次递归处理x
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
        
        largest_index = index
        if without_data is False:
            if left <= heap_size-1 and array[left][0] > array[index][0]:
                largest_index = left
            if right <= heap_size-1 and array[right][0] > array[largest_index][0]:
                largest_index = right
        else:
            if left <= heap_size-1 and array[left] > array[index]:
                largest_index = left
            if right <= heap_size-1 and array[right] > array[largest_index]:
                largest_index = right

        if largest_index != index:     # 如果父节点不是最大的，那么与对应最大的子节点交换位置，并继续递归判断下一级
            array[index], array[largest_index] = array[largest_index], array[index]
            self.max_heapify(array, largest_index, heap_size, without_data)

    def build_max_heap(self, array: list, without_data=True):
        """构建最大堆
        
        自底向上的对所有的非叶子节点的数进行最大堆堆化处理。(叶子节点的数会在处理其父节点时进行被处理)
        
        因为二叉堆可以可以看成一颗近似的完全二叉树，所以`index >= len(array)//2 + 1` 的都是叶子节点
        
        时间复杂度：:math:`O(n)`
        
        Args:
            array (list): 存放堆数据的数组
            without_data (bool): 如果为False，则期望每个元素应是一个二元元组，并将元组第一个元素作为值进行比较，默认为True
        """
        for index in range(len(array)//2, -1, -1):
            self.max_heapify(array, index, len(array), without_data)

    def extract_max(self, array: list):
        """弹出最大值
        
        这时假定执行该方法之前，对array已经进行了build_max_heap操作
        """
        return array.pop(0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()