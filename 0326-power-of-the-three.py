from math import floor, ceil, log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        result = log10(n)/log10(3)
        return result % 1 == 0
