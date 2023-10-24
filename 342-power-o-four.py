from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        result = log(n)/log(4)
        return result.is_integer()
