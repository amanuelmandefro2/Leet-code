class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort( key=lambda x : x < 0)   
        res = []
        print(nums)
        n = len(nums)//2 
        i = 0
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res


