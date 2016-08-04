# coding: utf-8


class Solution(object):
    def binarysearch(self, array, target):
        low = 0
        high = len(array)-1
        while(low<=high):
            mid = (low+high)/2
            midvalue = array[mid]

            if midvalue<target:
                low = mid +1
            elif midvalue>target:
                high = mid - 1
            else:
                return mid
        return None


if __name__=='__main__':
    a = [1,2,3,4,5,6,7]
    t = 8
    print Solution().binarysearch(a,t)