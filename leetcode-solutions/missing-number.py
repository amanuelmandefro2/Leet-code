class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_dict = {num:1 for num in nums}

        print(nums_dict)

        for num in range(len(nums) +1):
            if num not in nums_dict:
                return num      
        