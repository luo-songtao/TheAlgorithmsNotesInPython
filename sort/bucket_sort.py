"""
@Author  : luo-songtao
桶排序: 假设数据是均匀分布的.
    类似散列，将数散列或映射到按序号排列的桶中（使序号大的桶中的数均大于序号小的桶中的数）
    最后再利用如插排对每个桶单独排序，然后汇总所有的桶得出结果
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


def bucket_sort(array):
    max_item, min_item = max(array), min(array)
    bucket_quantity = len(array)    # 取桶数量为数组的长度
    range_mean = (max_item-min_item)/bucket_quantity    # 取级差平均值

    bucket_array = []
    for i in range(0, bucket_quantity):    # 初始化桶
        bucket_array.append([])

    for item in array:    # 将数映射到桶中，并使之满足序号大的桶中的数均大于序号小的桶中的数
        bucket_index = int((item-min_item)//range_mean)
        bucket_index = bucket_quantity - 1 if bucket_index >= bucket_quantity else bucket_index
        bucket_array[bucket_index].append(item)

    array.clear()
    for arr in bucket_array:
        insertion_sort(arr)    # 逐个排序
        array.extend(arr)


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    bucket_sort(the_array)
    print(the_array)