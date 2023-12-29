class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        op = 0
        max_elem = nums[0]
        i = 0
        while i < len(nums):
            if nums[i] != max_elem:
                op += i
                max_elem = nums[i]
            i += 1     
        return op
        
        