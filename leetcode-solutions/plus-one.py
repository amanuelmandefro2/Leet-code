class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        large_int = max(digits)

        idx_large = len(digits) - 1

        while digits[idx_large] + 1 > 9 and idx_large > -1:
                digits[idx_large] = 0
                idx_large -= 1
        if idx_large == -1:
            digits.insert(0, 1)
        else:
            digits[idx_large] += 1  
        print(digits)      
        return digits      
        