class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        max_val = max(nums)
        nums = set(nums)


        for i in range(1, max_val):
            if i not in nums:
                return i

        return max_val + 1 if max_val > 0 else 1        

        