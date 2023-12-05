class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r=[' ']*len(s)
        
        for i in range(len(s)):
            r[indices[i]]= s[i]
        return "".join(r)