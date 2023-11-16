class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trav_value = {}
        for i, num in enumerate(nums):
            if target - num in trav_value:
                return([trav_value[target-num], i])
            trav_value[num] = i
