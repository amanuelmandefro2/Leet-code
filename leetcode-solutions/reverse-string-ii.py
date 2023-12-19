class Solution:
    def reverseStr(self, s: str, k: int) -> str:

    
        res = ''
        i = 0

        while i < len(s):
            res += s[i:i + k][::-1]
            res += s[i + k:i + 2*k]
            i += 2*k 

        return res
