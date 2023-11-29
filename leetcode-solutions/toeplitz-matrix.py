class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False
        return True
       