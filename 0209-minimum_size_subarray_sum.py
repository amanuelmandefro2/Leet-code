class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        currsum = 0
        l = 0
        for r in range(len(nums)):
            currsum += nums[r]
            while currsum >= target:
                currsum -= nums[l]
                res = min(res, r-l+1)
                l += 1
        return 0 if res == float('inf') else res
