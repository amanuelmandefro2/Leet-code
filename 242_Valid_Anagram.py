class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for j in range(len(s)):
            countS[s[j]] = 1 + countS.get(s[j], 0)
            countT[t[j]] = 1 + countT.get(t[j], 0)
        for k in countS:
            if countS[k] != countT.get(k, 0):
                return False

        return True     
