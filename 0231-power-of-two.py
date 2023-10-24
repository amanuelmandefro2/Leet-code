from math import log
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 :
            return False
        result = log(n)/ log(2)
        return result.is_integer()
