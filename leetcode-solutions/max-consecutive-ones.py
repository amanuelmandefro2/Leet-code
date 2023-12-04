class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_1 = 0

        ans = 0

        for num in nums:
            if num == 1:
                ans += 1
                max_1 = max(max_1, ans)
            elif num == 0:
                ans = 0
        return max_1             
        