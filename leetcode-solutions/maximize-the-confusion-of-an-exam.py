class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_true = -float('inf')
        max_false = -float('inf')
        true_count = 0
        false_count = 0
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'F':
                false_count += 1
            while false_count > k:
                if answerKey[l] == 'F':
                    false_count -= 1
                l += 1
            max_true = max(max_true, r-l +1)  

        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                true_count += 1
            while true_count > k:
                if answerKey[l] == 'T':
                    true_count -= 1 
                l += 1
            max_false = max(max_false, r - l +1)  

        return max(max_true, max_false)
        