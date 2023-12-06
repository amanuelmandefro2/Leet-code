class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [num for num in nums if num < pivot]
        res += [num for num in nums if num == pivot]
        res += [num for num in nums if num > pivot]

        return res
        