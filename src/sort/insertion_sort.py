"""
@Author  : luo-songtao
插入排序
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        k = 1
        while i-k >= 0 and array[i-k] > current:
            array[i-k+1] = array[i-k]
            k += 1
        array[i-k+1] = current


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    insertion_sort(the_array)
    print(the_array)
