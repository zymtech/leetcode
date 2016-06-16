# -*- coding: utf-8 -*-


class Solution(object):
    """
    下排每个数都是先前上排那十个数在下排出现的次数。
    上排的十个数如下：
    【0，1，2，3，4，5，6，7，8，9】
    举一个例子，
    数值: 0,1,2,3,4,5,6,7,8,9
    分配: 6,2,1,0,0,0,1,0,0,0
    """

    # 求两个列表的乘积和
    def list_sum(self,a, b):
        size = len(a)
        c = [a[i] * b[i] for i in range(0, size)]
        # print c
        return sum(c)

        # 检查a每个元素中每个元素在b中出现的次数是否满足要求

    def check(self,a, b):
        for i in range(len(a)):
            if b.count(a[i]) != b[i]:
                return False
        return True

        # a 上排数组

    # b 下排数组
    # target 目标和(列表大小)
    # size 列表当前大小
    def calc(self,a, b, target, size):
        if 0 == size:
            if sum(b) == target and self.list_sum(a, b) == target:
                # print b, check(a, b)
                if self.check(a, b):
                    print a
                    print b
                    print '*' * 10
            return

        for i in range(0, target):
            b[size - 1] = a[i]
            if b[size - 1] * a[size - 1] <= target:
                self.calc(a, b, target, size - 1)

if __name__=='__main__':

    solution = Solution()
    a = [0,1 , 2, 3, 4, 5, 6, 7]
    b = [0 for i in range(0, 8)]
    solution.calc(a, b, 8, 8)
