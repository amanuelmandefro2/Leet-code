class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(b+a)
                if token == '*':
                    stack.append(b*a)
                if token == '/':
                    stack.append(int(b/a))
                if token == '-':
                    stack.append(b - a)
        return stack[0]

        