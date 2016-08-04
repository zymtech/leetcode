# -*- coding: utf-8 -*-


class Solution(object):
    def selectionsort(self, a):
        for i in xrange(len(a)-1):
            for j in xrange(i+1, len(a)-1):
                if a[j]<a[i]:
                    a[j], a[i] = a[i], a[j]
        return a


if __name__=='__main__':
    a = [1,4,3,2,6]
    print Solution().selectionsort(a)