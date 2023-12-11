class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #change nums list to set nums
        nums = set(nums)
       
        #assign maximum length of consecutive elements sequence to zero
        max_cons = 0

        #loop over nums set until we don't get maximum length by removing consequetive element from nums  sets  
        while max_cons < len(nums):
            random_num = nums.pop()
            longest_len = 1

            num = random_num
            while num + 1 in nums:
                longest_len += 1
                num = num +1
                nums.remove(num)

            num = random_num
            while num -1 in nums:
                longest_len += 1
                num = num -1
                nums.remove(num)  

            max_cons = max(max_cons, longest_len)      
            
        return max_cons        

     