class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        i = 0
        while i < min(len(word1), len(word2))*2:
            if i%2 == 0:
                merged += word1[i//2]
            else:
                merged += word2[i//2]
            i += 1
        merged += word1[i//2:]
        merged += word2[i//2:]

        return merged

        