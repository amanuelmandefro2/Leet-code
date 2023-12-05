class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        ghosts_distance = [0]*len(ghosts)
        

        for i  in range(len(ghosts)):
            ghosts_distance[i] = abs(ghosts[i][0] - target[0]) + abs(ghosts[i][1] - target[1])

        player_dist = abs(target[0]) + abs(target[1])
        return player_dist < min(ghosts_distance)
        