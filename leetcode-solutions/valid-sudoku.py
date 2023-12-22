from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box_3 = defaultdict(set)

        for i in range(len(board)): 
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in row[i] or 
                    board[i][j] in col[j] or 
                    board[i][j] in box_3[(i//3, j//3)]):
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box_3[(i//3, j//3)].add(board[i][j])

        return True
