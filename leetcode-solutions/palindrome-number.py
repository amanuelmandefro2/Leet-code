class Solution:
    def isPalindrome(self, x: int) -> bool:

        res = 0
        num = x
        while num > 0:
            last_digit = num % 10
            res = res *10 + last_digit
            num //= 10
        return res == x 
            
        