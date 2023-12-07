class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd_large = ''

        for i in range(len(num)-1,-1,-1):
          if not odd_large and int(num[i])%2 == 1:
            odd_large = num[i]
          elif odd_large:
            odd_large = num[i] + odd_large 

        return odd_large                
        