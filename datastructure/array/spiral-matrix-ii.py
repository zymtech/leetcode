# -*- coding: utf-8 -*-


class Solution(object):
    def generateMatrix(self, n):
        """
        leetcode 59
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for _ in range(n)] for i in range(n)]
        curr, left, right, top, bottom = 1, 0, n-1, 0, n-1
        while curr<=n*n:
            for i in range(left, right+1):
                result[top][i] = curr
                curr += 1
            for i in range(top+1, bottom+1):
                result[i][right] = curr
                curr += 1
            for i in range(right-1, left-1, -1):
                result[bottom][i] = curr
                curr += 1
            for i in range(bottom-1, top, -1):
                result[i][left] = curr
                curr += 1
            left, right, top, bottom = left+1, right - 1, top + 1, bottom - 1
        return result

if __name__ == "__main__":
    n = 4
    result = Solution().generateMatrix(n)
    for i in result:
        print i