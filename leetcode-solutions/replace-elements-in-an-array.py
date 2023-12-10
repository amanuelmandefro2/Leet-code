class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_idx ={}

        for i, num in enumerate(nums):
            num_idx[num] = i
    
        for operation in operations:
            nums[num_idx[operation[0]]] = operation[1]
            num_idx[operation[1]] = num_idx[operation[0]]

        return nums        
        