class Solution(object):
    """
    dp solution

    draw the matrxi down

    1 1 1 1  1  1  1
    1 2 3 4  5  6  7
    1 3 6 10 15 21 28

    for m = 7 n = 3
    return 28
    """
    def uniquePaths(self, m, n):
        if m < n:
            return self.uniquePaths(n, m)
        ways = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                ways[j] += ways[j - 1]
        return ways[-1]

class RecursiveSolution(object):
    """
    recursive solution: time limit exceed
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            return self.uniquePaths(n, m)
        return self.uniquePathsRecur(m,n)

    def uniquePathsRecur(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.uniquePathsRecur(m-1,n) + self.uniquePathsRecur(m, n-1)