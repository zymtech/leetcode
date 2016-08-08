# -*- coding: utf-8 -*-
# Time:  O(n^2)
# Space: O(1)
#
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#


class Solution(object):
    def generate(self, numRows):
        """
        :param numRows: int
        :return: a list of lists of integers
        """
        result = []
        for i in xrange(numRows):
            result.append([])
            for j in xrange(i+1):
                if j in [0,i]:
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
        return result


class Functional(object):
    def row(self,x):
        return ' '.join(map(str, reduce(lambda x, y: map(sum, zip([0] + x, x + [0])), range(x), [1])))

    def pascal(self, x):
        return '\n'.join(self.row(i).center(len(self.row(x - 1))) for i in range(x))

if __name__=='__main__':
    #print Solution().generate(5)
    print Functional().pascal(5)
