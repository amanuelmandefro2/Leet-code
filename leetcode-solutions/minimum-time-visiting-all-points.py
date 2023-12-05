class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        steps = 0
        i = 0
        while i < len(points) - 1:
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[i+1][0], points[i+1][1]

            steps += max(abs(x2-x1), abs(y2-y1))

            i+= 1
                 

        return  steps       
        