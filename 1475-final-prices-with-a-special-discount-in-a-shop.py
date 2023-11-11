class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = prices.copy()

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack[-1]] -= prices[i]
                stack.pop()
            stack.append(i)
        return res
