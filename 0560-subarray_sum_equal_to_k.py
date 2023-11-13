class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        res = 0
        sum = 0

        for num in nums:
            sum += num
            res += prefix.get(sum-k, 0)
            prefix[sum] = prefix.get(sum, 0) +1

        return res  
