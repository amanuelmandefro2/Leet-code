class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        num_pattern = 0
        for pattern in patterns:
            if pattern in word:
                num_pattern += 1
        return num_pattern 
