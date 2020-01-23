"""
@Author  : luo-songtao
希尔排序
"""
import math


def shell_sort(array):
    seq_count = int(math.log2(len(array)))
    for seq_number in range(1, seq_count+1):
        gap = 2 ** seq_number - 1    # 增量序列的间隔，···7、3、1
        for start_index in range(len(array)):    # 增量序列的起始下标
            """对增量序列进行插入排序"""
            for index in range(start_index+gap, len(array), gap):    # 增量序列的第2，3···个数的下标
                current = array[index]
                k = 1    # 增量序列中，位于index前的第k个
                while index-k*gap >= start_index and array[index-k*gap] > current:
                    array[index] = array[index-k*gap]
                    k += 1
                array[index-(k-1)*gap] = current


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    shell_sort(the_array)
    print(the_array)
