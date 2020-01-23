"""
@Author  : luo-songtao
最大子数组问题
"""
import math


def find_max_crossing_subarray(array, start, mid, stop):
    """
    寻找最大跨中间点的子数组的边界点
    (注意：这里找出的最大子数组，前提是在包含中间节点情况下，再找出与它组成最大子数组的情形，因此这里找出的数组长度至少为2)
    :param array: 待寻找的数组
    :param start: 起始下标
    :param mid: 中间下标
    :param stop: 结束下标
    :return: 左、右边界点，以及最大和
    """

    left_sum = - math.inf    # 记录mid左边的数和
    temp_sum = 0
    max_left = None
    for i in range(mid, start-1, -1):    # 从中间向左逐一遍历寻找
        temp_sum += array[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i    # 记录最大左边界

    right_sum = - math.inf
    temp_sum = 0
    max_right = None
    for i in range(mid+1, stop+1):    # 从中间向右逐一遍历寻找
        temp_sum += array[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = i    # 记录最大右边界

    return max_left, max_right, left_sum+right_sum


def find_maximum_subarray(array, start, stop):
    """
    寻找array中的最大的数组
    :param array: 待寻找的数组
    :param start: 起始下标
    :param stop: 结束下标
    :return: 最大子数组的起始下标和结束下标，以及该最大子数组的和
    """

    if stop - start == 1:    # 只剩一个元素那么直接返回
        return start, stop, array[start]
    else:
        # 取中间下标，如果长度为奇数，则向后取整
        mid = (start + stop)//2 if math.fmod(start + stop, 2) == 0 else 1 + (start + stop)//2
        # 递归求解左数组中最大的子数组
        left_start, left_stop, left_sum = find_maximum_subarray(array, start, mid)
        # 递归求解右数组中最大的子数组
        right_start, right_stop, right_sum = find_maximum_subarray(array, mid, stop)
        # 递归求解跨中间节点的最大子数组
        cross_start, cross_stop, cross_sum = find_max_crossing_subarray(array, start, mid, stop)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_start, left_stop, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_start, right_stop, right_sum
        else:
            return cross_start, cross_stop, cross_sum


if __name__ == '__main__':

    the_array = [13, -3, -25, -20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    start_index, end_index, maximum_sum = find_maximum_subarray(the_array, 0, 15)
    print(start_index, end_index, the_array[start_index:end_index+1], maximum_sum)