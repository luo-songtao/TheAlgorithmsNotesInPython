"""
@Author  : luo-songtao
计数排序: 基本原理
"""


def count_sort(array, k):
    """计数排序
    
    Args:
        array (list): 待排序数组
        k (int): 数组长度
    
    Returns:
        list: 新创建的已排序数组
    
    Example:
        >>> x = 10
        >>> x*x
        100
    
    """
    count_array = [0 for i in range(k+1)]
    result_array = [0 for i in range(len(array))]

    # 计数
    for i in range(len(array)):
        count_array[array[i]] += 1

    # 统计
    for i in range(1, k+1):
        count_array[i] += count_array[i-1]

    for j in range(len(array)-1, -1, -1):
        result_array[count_array[array[j]]-1] = array[j]
        count_array[array[j]] -= 1

    return result_array


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    result = count_sort(the_array, max(the_array))
    print(result)