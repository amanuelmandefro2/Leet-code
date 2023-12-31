class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        j = 0
        i = len(piles) - 2
        sum = 0
        while j < len(piles)//3:
            sum += piles[i]
            j += 1
            i -= 2
        return sum