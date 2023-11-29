class Solution:
    def isPalindrome(self, x: int) -> bool:

        res = 0
        num = x

        while num > 0:
            res = res *10 + num % 10
            num //= 10
            
        return res == x 
            
        