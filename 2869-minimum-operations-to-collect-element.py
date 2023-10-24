class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numsS = set()
        operation_count = 0
        for x in nums[::-1]:
            if 1 <= x <= k:
                numsS.add(x)
            operation_count += 1
            if len(numsS) == k:
                return operation_count
        
