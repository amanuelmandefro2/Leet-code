class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = s[:spaces[0]]
        res += ' '
        i = 1

        while i < len(spaces):
            res += s[spaces[i-1]:spaces[i]]
            res += ' '
            i += 1

        res += s[spaces[i - 1]: ]

        return res    