class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = Counter(p)
        anagCount = defaultdict(int)
        res = []
 
        for i in range(len(s)):
            if i >= len(p):
                if anagCount[s[i - len(p)]] == 1:
                    del anagCount[s[i - len(p)]]
                else:
                    anagCount[s[i - len(p)]] -= 1

            anagCount[s[i]] += 1

            if anagCount == pcount:
                res.append(i - len(p) + 1)
                
        return res