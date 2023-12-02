class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s):
            if len(s) > i + 2 and s[i+2] == '#':
                res += chr(int(s[i: i+2])+96)
                i += 3
            else:
                res += chr(int(s[i]) + 96)
                i += 1
        print(res)
        return res
        