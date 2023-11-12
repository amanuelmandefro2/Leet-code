class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l, r = 0, 0
        res = []
        last_occurance = {char:i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            r = max(r, last_occurance[char])

            if r == i:
                res.append(r - l +1)
                l = r+1
        return res
