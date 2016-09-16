# -*- coding: utf-8 -*-
# Time complexity O(n^2) , stable
# 插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
# 从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，
# 时间复杂度为O(n^2)。是稳定的排序方法。
# 插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，
# 但将最后一个元素除外（让数组多一个空间才有插入的位置），
# 而第二部分就只包含这一个元素（即待插入元素）。
# 在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。


class Solution(object):
    def insertion_sort(self, input_list):
        """
        :param input_list: list
        :return: list
        """
        for i in range(len(input_list)):
            for j in range(1, i+1)[::-1]:
                if input_list[j] < input_list[j-1]:
                    input_list[j-1], input_list[j] = input_list[j], input_list[j-1]
                else:
                    break
        return input_list

if __name__ == '__main__':
    input_list = [1,3,5,2,5,7]
    print Solution().insertion_sort(input_list)

