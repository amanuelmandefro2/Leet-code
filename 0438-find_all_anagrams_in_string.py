class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = {}
        res = []
        
        for e in p:
            pcount[e] = pcount.get(e, 0) + 1
        
        anagCount = {}
        for i in range(len(s)):
            if i >= len(p):
                if anagCount[s[i - len(p)]] == 1:
                    del anagCount[s[i - len(p)]]
                else:
                    anagCount[s[i - len(p)]] -= 1

            anagCount[s[i]] = anagCount.get(s[i], 0) + 1

            if anagCount == pcount:
                res.append(i - len(p) + 1)
        return res
