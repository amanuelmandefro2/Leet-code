class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]

        print(trans_matrix)
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                trans_matrix[c][r] = matrix[r][c]       


        return trans_matrix
        