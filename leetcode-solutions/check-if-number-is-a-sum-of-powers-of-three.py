class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        while n > 1:
            
            n, r = n//3, n%3
            if r == 2: return False

        return True
        