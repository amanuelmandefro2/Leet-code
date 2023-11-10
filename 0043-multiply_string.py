class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 =='0':
            return '0'
        def strToInt(s):
            res = 0
            i = 0

            while i < len(s):
                digit = ord(s[i]) - ord('0')
                res = res * 10 + digit
                i += 1
            return res
        def intToStr(n):
            res = ''

            while n > 0:
                digit = n % 10
                res = chr(digit + ord('0')) + res
                n //= 10
            return res
        return intToStr(strToInt(num1) * strToInt(num2))
        
