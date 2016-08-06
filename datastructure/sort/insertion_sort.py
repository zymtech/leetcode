# -*- coding: utf-8 -*-


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

