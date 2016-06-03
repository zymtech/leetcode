# -*-coding: utf8 -*-
import math

class Solution:
    """
    plate number
    the answer is 7744
    """
    def solution(self):
        """

        :return: int
        """
        candidate = [x*x for x in range(int(math.sqrt(9999)))]
        for i in candidate:
            if i>999 and str(i)[0]==str(i)[1] and str(i)[2]==str(i)[3]:
                print i


if __name__=='__main__':
    solution = Solution()
    solution.solution()