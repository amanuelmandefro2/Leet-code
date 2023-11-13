class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        l, r = 0, len(nums) -1
        while r >= 0 and l < len(nums):
            if l == r:
                continue
            else:
                answer[l] *= nums[r]
            if r == 0 and l < len(n):
                l+=1
                r = len(nums) -1
            else:
                r -= 1


        return answer
