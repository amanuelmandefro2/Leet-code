class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        can_buy = 0

        for cost in costs:
            if cost <= coins:
                coins -= cost
                can_buy += 1
            else:
                break

        return can_buy            
        