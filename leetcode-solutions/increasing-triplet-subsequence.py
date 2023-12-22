class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        x, y, z = nums[0], float('inf'), float('inf')

        for i in range(len(nums)):
            if x >= nums[i]:
                x = nums[i]
            elif y >= nums[i]:
                y = nums[i]
            else:
               return True

        return False            



              


        