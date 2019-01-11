# Q) Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0
#code
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = set() 
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if tuple(list([i,j])) not in l:
                        
                        for k in range(len(matrix)):
                            if matrix[k][j] !=0:
                                l.add(tuple(list([k,j])))
                                matrix[k][j] = 0
                        for k in range(len(matrix[i])):
                            if matrix[i][k]!=0:
                                l.add(tuple(list([i,k])))
                                matrix[i][k] = 0