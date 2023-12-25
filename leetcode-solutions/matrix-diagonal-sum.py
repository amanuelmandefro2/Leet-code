class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        idx_lst = []
        sum_diagonal = 0
        r, c = 0, 0
        while r < len(mat) and c < len(mat[0]):
            idx_lst.append([r, c])
            sum_diagonal += mat[r][c]
            r += 1
            c += 1
    

        r, c = 0, len(mat[0]) - 1
        while r < len(mat) and c >= 0:
            
            if [r, c] not in idx_lst:
                sum_diagonal += mat[r][c]
                mat[r][c]
            r += 1
            c -= 1
        return sum_diagonal        


        