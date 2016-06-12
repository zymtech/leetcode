# -*- coding: utf-8 -*-


class solution(object):
    """
    biggest submatrix
    time complexity : O(n square)
    """
    @classmethod
    def solution(cls,matrix):
        """

        :param matrix: List[List]
        :return: List[list]
        """
        global max
        max= [0,0,0]
        for i,l in enumerate(matrix):
            for j in range(len(l)):
                if i+1<= len(matrix)-1 and j+1<=len(matrix[0])-1:
                    if matrix[i][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i+1][j+1]>max[0]:
                        max = [matrix[i][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i+1][j+1], i,j]
        print max[0], matrix[max[1]][max[2]]


if __name__=='__main__':
    matrix = [[1,2,3],[4,5,5],[7,7,0]]
    solution.solution(matrix)
