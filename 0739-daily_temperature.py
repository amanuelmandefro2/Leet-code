class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                len_day = i - stack[-1]
                res[stack[-1]] = len_day
                stack.pop()
            stack.append(i)
        return res

        """
        brute force solution 
        for i in range(len(temperature)):
            for j in range(i+1, len(temperature)):
                if temperature[j] > temperature[i]:
                    res[i] = j - i
                    break
        return res

        """
