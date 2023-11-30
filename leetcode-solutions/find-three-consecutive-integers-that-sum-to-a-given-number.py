class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        x = (num - 3)//3

        return [x, x+1, x+2] if 3*x+3 == num else []
        