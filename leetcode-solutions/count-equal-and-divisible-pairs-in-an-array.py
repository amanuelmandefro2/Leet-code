class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pair_count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    pair_count += 1
        return pair_count            

        