class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        i = 0
        max_sum = -float('inf')
        i = 0
        while i + 2 < len(grid):
            j = 0

            while j + 2 < len(grid[0]):
                curr_sum = sum(grid[i][j: j+3])
                curr_sum += grid[i+1][j+1]
                curr_sum += sum(grid[i+2][j:j+3])
                max_sum =max(max_sum, curr_sum)
                j += 1
            i += 1     

        return  max_sum 

             

            
