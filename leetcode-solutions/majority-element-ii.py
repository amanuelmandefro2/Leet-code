class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if nums.count(num) > len(nums) // 3 and num not in res:
                res.append(num)
        return res        
        