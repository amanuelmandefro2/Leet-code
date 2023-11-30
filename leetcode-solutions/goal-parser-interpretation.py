class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    res += 'o'
                else:
                    res += command[i+1]
                i += 1
            elif command[i] == ')':
                i += 1
                continue
            else:
                res += command[i]
            i += 1
        return res