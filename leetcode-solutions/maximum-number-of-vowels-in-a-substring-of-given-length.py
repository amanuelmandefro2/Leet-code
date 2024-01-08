class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowel = {'a', 'e','i', 'o','u'}
        vowel_cons = 0
        for i in range(k):
            if s[i] in vowel:
                vowel_cons += 1
        max_vow = vowel_cons
        for i in range(k, len(s)):
            if s[i-k] in vowel:
                vowel_cons -= 1
            if s[i] in vowel:
                vowel_cons += 1
            max_vow = max(max_vow, vowel_cons) 
        return max_vow           

        