class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_lines = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []

        for line in keyboard_lines:

            for word in words:
                if set(word.lower()).issubset(set(line)):
                    res.append(word)
        return res