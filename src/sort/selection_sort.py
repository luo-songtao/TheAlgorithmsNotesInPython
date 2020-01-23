"""
@Author  : luo-songtao
选择排序
"""


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != i:
            array[min_index], array[i] = array[i], array[min_index]


def selection_sort2(array):
    for i in range(len(array)//2+1):
        min_index = i
        max_index= len(array) - 1 - i
        if array[min_index] >= array[max_index]:
            array[min_index], array[max_index] = array[max_index], array[min_index]
        for j in range(i+1, len(array)-i):
            if array[min_index] > array[j]:
                min_index = j
            elif array[max_index] < array[j]:
                max_index = j
        if min_index != i:
            array[min_index], array[i] = array[i], array[min_index]
        if max_index != len(array) - 1 - i:
            array[max_index], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[max_index]


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    selection_sort2(the_array)
    print(the_array)
