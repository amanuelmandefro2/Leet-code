class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        maxAvg = currSum/k
        
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k] 
            maxAvg = max(maxAvg, currSum/k)
        return maxAvg

        