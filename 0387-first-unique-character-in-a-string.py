class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_hashmap = {}
        for i in range(len(s)):
            char_hashmap[s[i]] = 1 + char_hashmap.get(s[i], 0)
        for char in char_hashmap:
            if char_hashmap[char] == 1:
                return s.index(char)
            
        return -1
        
