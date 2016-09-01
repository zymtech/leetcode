# -*- coding: utf-8 -*-


class Solution(object):
    def spiralmatrix(self, matrix):
        """
        leetcode 54
        :param matrix: List[List[int]]
        :return: List[int]
        """
        if not matrix:
            return []

        result, left, right, top, bottom = [], 0, len(matrix[0])-1, 0, len(matrix)-1

        while left <= right and top <= bottom:
            for i in xrange(left, right+1):
                result.append(matrix[top][i])
            for i in xrange(top+1, bottom):
                result.append(matrix[i][right])
            for i in xrange(right, left-1, -1):
                if top < bottom:
                    result.append(matrix[bottom][i])
            for i in xrange(bottom-1, top, -1):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return result

if __name__ == "__main__":
    matrix = [
        [1,2,4],
        [4,3,5],
        [7,8,9]
    ]
    print Solution().spiralmatrix(matrix)