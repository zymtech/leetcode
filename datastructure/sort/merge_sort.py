# -*- coding: utf-8 -*-
# stable
# time complexity O(nlog2n)
# 归并排序是建立在归并操作上的一种有效的排序算法,
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
# 将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
# 若将两个有序表合并成一个有序表，称为二路归并。

#归并过程为：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，
# 并令i和k分别加上1；否则将第二个有序表中的元素a[j]复制到r[k]中，
# 并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，
# 然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。
# 归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，
# 接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。


class MergeSort(object):
    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def merge_sort(self, lists):
        if len(lists) <= 1:
            return lists
        num = len(lists)/2
        left = self.merge_sort(lists[:num])
        right = self.merge_sort(lists[num:])
        return self.merge(left, right)


if __name__ == "__main__":
    lists = [3,23,242,3,3,34,33]
    print MergeSort().merge_sort(lists)
