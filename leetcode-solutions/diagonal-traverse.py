from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # if not mat or not mat[0]:
        #     return []

        # m, n = len(mat), len(mat[0])
        # ans = []
        # r, c = 0, 0
        # direction = 1  # 1 for upward, -1 for downward

        # for _ in range(m * n):
        #     ans.append(mat[r][c])
        #     r -= direction
        #     c += direction

        #     if r >= m:
        #         r = m - 1
        #         c += 2
        #         direction = -direction
        #     elif c >= n:
        #         c = n - 1
        #         r += 2
        #         direction = -direction
        #     elif r < 0:
        #         r = 0
        #         direction = -direction
        #     elif c < 0:
        #         c = 0
        #         direction = -direction

        # return ans
        index_values = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                index_values[r+c].append(mat[r][c])
        ans = []
        for idx in index_values:
            if idx % 2 == 0:
                ans += index_values[idx][::-1]
            else:    
                ans += index_values[idx]
        return ans            
