class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0 for _ in range(n)] for _ in range(m)]
        
        for guard in guards:
            mat[guard[0]][guard[1]] = 'G'
        for wall in walls:
            mat[wall[0]][wall[1]] = 'W'    

        for guard in guards:
            r = guard[0]
            c = guard[1]
            i = r
            j = c + 1

            while j < n and mat[i][j] != 'G':
                if mat[i][j] == 'W':
                    break
                mat[i][j] = 1
                j += 1
            i = r+1
            j = c
            while i < m and mat[i][j] != 'G':
                if mat[i][j] == 'W':
                    break
                mat[i][j] = 1
                i += 1 
            j = c - 1
            i = r    
            while j > -1 and mat[i][j] != 'G':
                if mat[i][j] == 'W':
                    break
                mat[i][j] = 1
                j -= 1 
            j = c
            i = r -1    
            while i > -1  and mat[i][j] != 'G':
                if mat[i][j] == 'W':
                    break
                mat[i][j] = 1
                i -= 1 
        unguarded = 0

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    unguarded += 1

                
                         
        return unguarded
  
        