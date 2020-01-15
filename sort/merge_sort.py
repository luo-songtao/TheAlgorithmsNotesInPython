"""
@Author  : luo-songtao
归并排序
"""
import math


def merge(array, start, mid, stop):
    left = array[start:mid]
    right = array[mid:stop+1]

    sentry = math.inf
    left.append(sentry)
    right.append(sentry)

    left_cursor, right_cursor = 0, 0

    for i in range(start, stop+1):
        if left[left_cursor] <= right[right_cursor]:
            array[i] = left[left_cursor]
            left_cursor += 1
        else:
            array[i] = right[right_cursor]
            right_cursor += 1


def merge_sort(array, start, stop):
    """
    O(nlg n )
    :param array:
    :param start:
    :param stop:
    :return:
    """
    if start + 1 < stop:
        mid = (start + stop) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, stop)
        merge(array, start, mid, stop)


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    merge_sort(the_array, 0, len(the_array) - 1)
    print(the_array)