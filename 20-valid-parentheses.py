class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(' , '}':'{', ']':'['}

        for p in s:
            if p in parentheses.values():
                stack.append(p)
            elif stack and parentheses[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
