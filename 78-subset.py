class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(start, temp, output):
            output += [temp]
            for i in range(start, len(nums)):
                helper(i+1, temp+[nums[i]], output)
        helper(0, [], output)
        return output
        
