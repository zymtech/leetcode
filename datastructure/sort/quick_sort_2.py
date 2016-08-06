# -*- coding: utf-8 -*-


class Solution(object):
    def quick_sort(self, array, start, end):
        if start < end:
            pivot_index = self.partition(array, start, end)
            self.quick_sort(array, start, pivot_index)
            self.quick_sort(array, pivot_index+1, end)

    def partition(self, array, start, end):
        pivot_index = start
        pivot = array[start]
        for i in xrange(start+1, end+1):
            if array[i] < pivot:
                pivot_index += 1
                if pivot_index != i:
                    array[i], array[pivot_index] = array[pivot_index], array[i]
        array[start], array[pivot_index] = array[pivot_index], array[start]
        return pivot_index

if __name__=='__main__':
    array = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
    Solution().quick_sort(array, 0, len(array)-1)
    print array