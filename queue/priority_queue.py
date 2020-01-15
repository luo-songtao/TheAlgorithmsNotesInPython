"""
@Author  : luo-songtao
优先级队列
"""
import math


class PriorityQueue:

    @staticmethod
    def heap_maximum(array):
        return array[0]

    @staticmethod
    def get_parent_index(index: int):
        return index / 2 if math.fmod(index, 2) == 0 else (index - 1) / 2

    @staticmethod
    def get_left_child_index(index: int):
        return 2 * index

    @staticmethod
    def get_right_child_index(index: int):
        return 2 * index + 1

    def max_heapify(self, array, index: int, heap_size: int):
        """
        堆化：将指定索引处的数调整到堆的合适位置
        (最大堆：父节点必须大于等于左右子节点)
        O(lg n)
        :param array:
        :param index:
        :param heap_size: 当前堆的大小
        :return:
        """
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)

        largest_index = index

        if left <= heap_size - 1 and array[left] > array[index]:
            largest_index = left

        if right <= heap_size - 1 and array[right] > array[largest_index]:
            largest_index = right

        if largest_index != index:
            array[index], array[largest_index] = array[largest_index], array[index]
            self.max_heapify(array, largest_index, heap_size)

    def heap_extract_max(self, array, heap_size: int):
        max = array[0]
        array[0] = array[heap_size-1]
        heap_size -= 1
        self.max_heapify(array, 0, heap_size)
        return max

    def heap_increase_key(self, array, index, key):

        array[index] = key
        parent_index = self.get_parent_index(index)
        while index > 1 and array[parent_index] < array[index]:
            array[index], array[parent_index] = array[parent_index], array[index]
            index = parent_index
            parent_index = self.get_parent_index(index)

    def max_heap_insert(self, array, key, heap_size):
        heap_size += 1
        array[heap_size] = - math.inf
        self.heap_increase_key(array, heap_size, key)

    