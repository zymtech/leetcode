# -*- coding: utf-8 -*-


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = []
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if j in [0,i]:
                    row.append(1)
                else:
                    row.append(ret[i-1][j-1] + ret[i-1][j])
            ret.append(row)
        return ret[-1]

class Solution2(object):
    """
    list comprehension
    """
    def getRow(self, rowIndex):
        result = [1]
        for i in range(1, rowIndex + 1):
            result = [1] + [result[j-1] + result[j] for j in range(1,i)] + [1]
        return result

if __name__=='__main__':
    print Solution().getRow(4)
    print Solution2().getRow(4)