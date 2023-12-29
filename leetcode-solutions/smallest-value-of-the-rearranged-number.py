class Solution:
    def smallestNumber(self, num: int) -> int:
        sign = None
        if num < 0: 
            sign = '-'
            num = -1 * num
    

        nums = list(str(num))
        if sign == '-':
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i]+nums[j] < nums[j] + nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
        else:                
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i]+nums[j] > nums[j]+nums[i]:
                        if i == 0 and nums[j] == '0':
                            continue
                        else:
                            nums[i], nums[j]  = nums[j], nums[i]   
        
        return  - int(''.join(nums)) if sign == '-' else int(''.join(nums))
        