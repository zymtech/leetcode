# -*- coding: utf-8 -*-
# shell sort is a improved version of insertion sort.
# unstable
# 也称缩小增量排序
# 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
# 随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。


class ShellSort(object):
    def shell_sort(self, lists):
        count = len(lists)
        step = 2
        group = count/step
        while group > 0:
            for i in range(0, group):
                j = i + group
                while j < count:
                    k = j - group
                    key = lists[j]
                    while k >= 0:
                        if lists[k] > key:
                            lists[k + group] = lists[k]
                            lists[k] = key
                        k -= group
                    j += group
            group /= step
        return lists

if __name__=="__main__":
    lists = [3,24,2,5,12]
    print ShellSort().shell_sort(lists)
