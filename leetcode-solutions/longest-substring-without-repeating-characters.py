class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length