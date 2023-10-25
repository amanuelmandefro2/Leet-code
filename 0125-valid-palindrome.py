class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLower = s.lower()
        sletter = ''
        if s== " ":
            return True
        for char in sLower:
            if char.isalnum():
                sletter += char
        i, j = 0, len(sletter) - 1
        for _ in range(len(sletter)):
            if sletter[i] != sletter[j]:
                return False
            i += 1
            j -= 1
        return True
