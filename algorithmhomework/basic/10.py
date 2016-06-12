# -*- coding: utf-8 -*-


class Solution(object):
    """
    实现1+2+...+n,不使用乘除、for、while、if、else、switch、case
    :param n:
    :return: int
    """
    @classmethod
    def solution(self, n):
        list = range(1, n+1)
        list1 = range(n, 0, -1)
        #print list, list1
        result = map(lambda x, y: x+y, list, list1)
        return sum(result)/2

if __name__=='__main__':
    n= 10
    print Solution.solution(n)
