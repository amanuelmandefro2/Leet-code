from math import log, floor, ceil
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 :
            return False
        return floor(log2(n)) == ceil(log2(n))
        
