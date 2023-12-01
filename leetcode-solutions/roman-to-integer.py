class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i = 0
        while i < len(s):
            if roman_map[s[i]] > roman_map[s[i - 1]] and i > 0:
                res += roman_map[s[i]] - roman_map[s[i - 1]] * 2
                i += 1
            else:
                res += roman_map[s[i]]
                i += 1
        return res
