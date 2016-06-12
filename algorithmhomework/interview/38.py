# -*- coding: utf-8 -*-


class Solution():
    """
    (1) Fibonacci
    """
    a1 = 0
    a2 = 1
    sum = 0
    print a1
    @classmethod
    def solution(self,n):
        for i in range(n-2):
            print self.a2
            self.sum = self.a1 + self.a2
            self.a1= self.a2
            self.a2 = self.sum
        return self.sum

if __name__=='__main__':
    print Solution.solution(5)




"""
(2) draw 10 lines through 9 dots
#      #      #
   #   #   #
#      #      #
"""