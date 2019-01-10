# Q) Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# 	 write a method to rotate the image by 90 degrees. Can you do this in place?
#code
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        i = 0
        for item in list(map(list, zip(*matrix))):

            matrix[i] =  list(reversed(item))
            i+=1