class Solution(object):
    def isValidSudoku(self,board):
        """

        :param board: List[List[str]]
        :return: bool
        """
        if not board:
            return False
        for i in board:
            if not self.isValidList(i):
                return False
        for i in range(9):
            if not self.isValidList([board[j][i] for j in range(9)]):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isValidList([board[m][n] for m in range(3*i,3*i+3)\
                                         for n in range(3*j, 3*j+3)]):
                    return False
        return True

    def isValidList(self, list):
        list = filter(self.filterFunc, list)
        return len(set(list)) == len(list)

    def filterFunc(self, char):
        if char != '.':
            return char

if __name__ == "__main__":
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    board2 = ["....5..1.",
              ".4.3.....",
              ".....3..1",
              "8......2.",
              "..2.7....",
              ".15......",
              ".....2...",
              ".2.9.....",
              "..4......"]
    print Solution().isValidSudoku(board2)
