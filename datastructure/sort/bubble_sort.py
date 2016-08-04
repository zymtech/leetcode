# -*- coding: utf-8 -*-


class solution(object):
    def bubblesort(self, a):
        for _ in xrange(len(a)-1):
            for i in range(len(a)-1):
                if a[i]>a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
        return a

if __name__ == '__main__':
    a = [3,2,6,1,7]
    print solution().bubblesort(a)
