"""
@Author  : luo-songtao
排序算法：堆排序
"""
import math


class HeapSort:

    @staticmethod
    def get_parent_index(index: int):
        return index/2 if math.fmod(index,2) == 0 else (index-1)/2

    @staticmethod
    def get_left_child_index(index: int):
        return 2*index

    @staticmethod
    def get_right_child_index(index: int):
        return 2*index + 1

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

        if left <= heap_size-1 and array[left] > array[index]:
            largest_index = left

        if right <= heap_size-1 and array[right] > array[largest_index]:
            largest_index = right

        if largest_index != index:     # 如果父节点不是最大的，那么与对应最大的子节点交换位置，并继续递归判断下一级
            array[index], array[largest_index] = array[largest_index], array[index]
            self.max_heapify(array, largest_index, heap_size)

    def build_max_heap(self, array):
        """
        构建最大堆，堆所有非叶子节点进行最大堆堆化判断
        O(n)
        :param array:
        :return:
        """
        # index >= len(array)//2 + 1 的都是叶子节点
        for index in range(len(array)//2, -1, -1):
            self.max_heapify(array, index, len(array))

    def heap_sort(self, array):
        """
        堆排主逻辑
        O(nlg n)
        :param array:
        :return:
        """
        self.build_max_heap(array)    # 此时已经构建出最大堆，第一个元素必定是最大值
        heap_size = len(array)
        # 1. 将第一个元素和最后一个置换位置，并将它剔除出堆中
        # 2. 对剩下的元素重新调整以出现新的最大堆, 回到第一步，直到只剩一个元素
        # 那么最终array将是一个升序的排列
        for i in range(len(array)-1, 0, -1):
            array[0], array[i] = array[i], array[0]
            heap_size -= 1
            self.max_heapify(array, 0, heap_size)


if __name__ == '__main__':
    the_array = [41,22,36,7,21,27,18,3,79,8,43,27,45,36,84,7,47]
    HeapSort().heap_sort(the_array)
    print(the_array)