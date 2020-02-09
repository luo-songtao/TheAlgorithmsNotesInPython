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


class BinaryMaxHeap:
    
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

    def max_heapify(self, array: list, index: int, heap_size: int):
        """最大堆堆化处理，维护最大堆的性质
        
        最大堆性质：父节点必须大于等于左右子节点
        
        根据最大堆的性质将指定索引处的数调整到堆的它合适的位置
            - 将指定index处的值x与其左右孩子的进行比较，将最大的孩子与其交换位置，以满足最大堆性质，并再次递归处理x
            - 当指定index处的值x比其左右孩子的都大，则不用再递归

        时间复杂度：:math:`O(lg n)`,n表示堆大小
        
        Args:
            array (list): 存放堆数据的数组
            index (int): 指定的索引
            heap_size (int): 当前堆有效元素个数。(array[0:heap_size-1]中存放的才是堆上有效的元素)
        """
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        
        largest_index = index
        if left <= heap_size-1 and array[left] > array[index]:
            largest_index = left

        if right <= heap_size-1 and array[right] > array[largest_index]:
            largest_index = right

        if largest_index != index:     # 如果父节点不是最大的，那么与对应最大的子节点交换位置，并继续递归判断下一级
            array[index], array[largest_index] = array[largest_index], array[index]
            self.max_heapify(array, largest_index, heap_size)

    def build_max_heap(self, array: list):
        """构建最大堆
        
        自底向上的对所有的非叶子节点的数进行最大堆堆化处理。(叶子节点的数会在处理其父节点时进行被处理)
        
        因为二叉堆可以可以看成一颗近似的完全二叉树，所以`index >= len(array)//2 + 1` 的都是叶子节点
        
        时间复杂度：:math:`O(n)`
        
        Args:
            array (list): 存放堆数据的数组
        """
        for index in range(len(array)//2, -1, -1):
            self.max_heapify(array, index, len(array))


if __name__ == '__main__':
    the_array = [41,22,36,7,21,27,18,3,79,8,43,27,45,36,84,7,47]
    heap_sort(the_array)
    print(the_array)