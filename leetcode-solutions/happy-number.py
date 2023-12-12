class Solution:
    def isHappy(self, n: int) -> bool:


        while n >= 5:
            new_num = 0
            while n > 0:
                new_num = new_num + (n % 10) ** 2
                n = n // 10
            n = new_num

        return n == 1
  

