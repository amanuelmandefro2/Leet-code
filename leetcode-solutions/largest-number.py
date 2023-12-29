class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
          
        ans = ''

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                
                        
        ans = ''.join(nums)


               
        return '0' if int(ans) == 0 else ans    