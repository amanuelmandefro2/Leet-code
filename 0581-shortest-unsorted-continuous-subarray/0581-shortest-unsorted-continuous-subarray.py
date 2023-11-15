class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        
        l = float('inf')
        r = 0

        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                r = max(r, i)
                l = min(l, i)
        return 0 if l == float('inf') or r == 0 else r - l + 1
        
        
            

