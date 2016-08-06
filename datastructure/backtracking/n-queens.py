# -*- coding: utf-8 -*-


class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        self.ret = 0
        self.limit = n
        self.solveNQueens(0, [])
        return self.ret

    def solveNQueens(self, row, queens):
        if row == self.limit:
            self.ret += 1
            self.printBoard(queens)
        else:
            for col in xrange(self.limit):
                if self.check(queens, row, col):
                    queens.append([row, col])
                    self.solveNQueens(row + 1, queens) # 搜索下一行
                    queens.pop()

    def check(self, queens, row, col):
        for queen in queens:
            if (col == queen[1]) or (abs(row - queen[0]) == abs(col - queen[1])):
                return False
        return True

    def printBoard(self, queens):
        board = [['.' for col in range(self.limit)] for row in range(self.limit)]
        for queen in queens:
            board[queen[0]][queen[1]] = 'Q'
        for _ in range(self.limit):
            print board[_]
            print
        print '-------------------'

if __name__=='__main__':
    print Solution().totalNQueens(5)


