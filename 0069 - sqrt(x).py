class Solution:
    def mySqrt(self, x: int) -> int:
      num = 0
      while 1:
        if num * num < x:
            num += 1
        elif num * num == x:
            return num
        elif num * num > x:
            return num - 1
