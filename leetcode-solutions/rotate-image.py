from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_top, r_bottom = 0, len(matrix) - 1
        
        while r_top < r_bottom:
            matrix[r_top], matrix[r_bottom] = matrix[r_bottom],  matrix[r_top]
            r_top += 1
            r_bottom -= 1
            
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
