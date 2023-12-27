class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        max_val = 0
        count =0
        for i in range(len(flips)):
            if max_val < flips[i]:
                max_val = flips[i]
            if max_val == i+1:
                count += 1

        return count            