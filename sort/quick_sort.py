"""
@Author  : luo-songtao
快排
"""


class QuickSort:

    def quick_sort(self, array, start, stop):
        """
        最差：O(n^2):  n(n-1)(n-2)···2
        最优:O(nlg n)
        平均:O(nlg n)
        :param array:
        :param start:
        :param stop:
        :return:
        """
        if start < stop:
            bound = self.partition(array, start, stop)
            self.quick_sort(array, start, bound-1)
            self.quick_sort(array, bound+1, stop)

    def partition(self, array, left_bound, right_bound):
        """
        O(n)
        :param array:
        :param left_bound:
        :param right_bound:
        :return:
        """
        compared_target = array[right_bound]
        bound = left_bound
        for i in range(left_bound, right_bound):
            if array[i] <= compared_target:
                array[i], array[bound] = array[bound], array[i]
                bound += 1
        array[bound], array[right_bound] = array[right_bound], array[bound]
        return bound


import random


class QuickSort2:

    def quick_sort(self, array, start, stop):
        """
        :param array:
        :param start:
        :param stop:
        :return:
        """
        while start < stop:
            bound = self.random_partition(array, start, stop)
            self.quick_sort(array, start, bound-1)
            start = bound + 1

    def random_partition(self, array, left_bound, right_bound):
        random_target = random.randrange(left_bound, right_bound)
        array[right_bound], array[random_target] = array[random_target], array[right_bound]
        return self.partition(array, left_bound, right_bound)

    def partition(self, array, left_bound, right_bound):
        """
        O(n)
        :param array:
        :param left_bound:
        :param right_bound:
        :return:
        """
        compared_target = array[right_bound]
        bound = left_bound
        for i in range(left_bound, right_bound):
            if array[i] <= compared_target:
                array[i], array[bound] = array[bound], array[i]
                bound += 1
        array[bound], array[right_bound] = array[right_bound], array[bound]
        return bound


if __name__ == '__main__':
    the_array = [41, 22, 36, 7, 21, 27, 18, 3, 79, 8, 43, 27, 45, 36, 84, 7, 47]
    QuickSort().quick_sort(the_array, 0, len(the_array)-1)
    print(the_array)