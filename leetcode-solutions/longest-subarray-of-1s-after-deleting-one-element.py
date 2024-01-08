class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(0) == 0:
            return len(nums) -1

        i, count = 0, 0
        max_length = 0
        while i < len(nums):
            if nums[i] == 0:
                i += 1
        
                if i < len(nums) and nums[i] != 0:
                    j = i
                    while j < len(nums) and nums[j] != 0:
                        j += 1
                        count += 1 
                    max_length = max(count, max_length)

                count = 0
            else:
                count += 1
                i += 1 
                max_length = max(count, max_length)
        return max_length               
            
        