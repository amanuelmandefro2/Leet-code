class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = n
        while not(i % n == 0 and i % 2 ==0):
            i += n
        return i
        