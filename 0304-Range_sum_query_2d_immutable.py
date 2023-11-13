class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.prefix =  [[0] * (col + 1) for r in range((row + 1))]

        for i in range(row):
            rowprefix = 0
            for j in range (col):
                rowprefix += matrix[i][j]
                above = self.prefix[i][j + 1]
                self.prefix[i+1][j+1] = rowprefix + above 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefix[row2 + 1][col2 + 1]
        bottomLeft = self.prefix[row2 +1][col1]
        topRight = self.prefix[row1][col2+1]
        topleft = self.prefix[row1][col1]
        return bottomRight - bottomLeft -topRight + topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
