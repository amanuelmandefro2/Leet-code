import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLower = s.lower()
        l, r = 0, len(s) -1
        while l < r:
            while l < r and not sLower[l].isalnum():
                l+=1
            while l<r and not sLower[r].isalnum():
                r -= 1
            if sLower[r] != sLower[l]:
                return False
            r -= 1
            l += 1
            
        return True


        