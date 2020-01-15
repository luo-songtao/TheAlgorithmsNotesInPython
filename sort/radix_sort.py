"""
@Author  : luo-songtao
基数排序
"""
import math


def radix_sort(array, base=10):
    max_item = max(array)
    places = math.floor(math.log(max_item, base))    # 最大值的位数

    digits_array = [[] for i in range(base)]
    for i in range(places+1):    # 从最低位开始依次进行排序

        for item in array:    # 根据对应位的数字进行分类(分桶)
            digit_number = (item//(base**i)) % base
            digits_array[digit_number].append(item)

        array.clear()
        for arr in digits_array:    # 按照位数值从低到高重新组合新的数组
            array.extend(arr)
            arr.clear()


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    radix_sort(the_array)
    print(the_array)

