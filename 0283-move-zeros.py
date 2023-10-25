class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCounter = nums.count(0)
        nextNonZero = 0

        for n in nums:
            if n != 0:
                nums[nextNonZero] = n
                nextNonZero += 1
        for zero in range (1, zeroCounter + 1):
            nums[-zero] = 0
  
