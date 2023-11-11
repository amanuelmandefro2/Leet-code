class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        res = ''
        if k == len(num):
            return '0'
        count = 0
        for i in range(len(num)):
            while stack and int(stack[-1]) > int(num[i])  and count < k:
                stack.pop()
                count += 1
            stack.append(num[i])
        while  count < k:
            stack.pop()
            count += 1
        res = ''.join(stack).lstrip('0')
        
        return '0' if not res else res
