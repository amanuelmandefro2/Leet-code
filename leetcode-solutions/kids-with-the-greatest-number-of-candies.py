class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)

        for i in range(len(candies)):
            el = candies.pop(i)
            if el + extraCandies >= max(candies):
                res[i] = True
            candies.insert(i, el)
        return res        