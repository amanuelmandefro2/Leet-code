class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cons_count = 1
        lst = []
        for i in range(1, len(num)):
            if num[i] == num[i - 1]:
                cons_count += 1
            else:
                cons_count = 1
            if cons_count == 3:
                lst.append(num[i]) 
                                          
        return "" if len(lst) == 0 else max(lst) * 3       


        