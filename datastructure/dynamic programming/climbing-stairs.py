# -*- coding: utf-8 -*-


class Solution(object):
    """DP solution"""
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        ways = [1,2]
        if n in [1,2]:
            return ways[n-1]
        for i in range(2,n):
            ways.append(ways[i-1]+ways[i-2])
        return ways[-1]


class Solution2(object):
    """recursive solution"""
    def climbStairs(self, n):
        if not n:
            return 0
        ways = [1,2]
        if n in [1,2]:
            return ways[n-1]
        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__=='__main__':
    print Solution().climbStairs(10)
    print Solution2().climbStairs(10)