class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new_word1 = ''
        for char in word1:
            new_word1 += char
        new_word2 = ''
        for char in word2:
            new_word2 += char
        return  new_word1 == new_word2      
        