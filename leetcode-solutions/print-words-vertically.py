class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_lst = s.split()
        print(s_lst)
        max_length = 0
        for si in s_lst:
            max_length = max(max_length, len(si))
        ans = []  

        for i in range(max_length):
            in_str = ''
            for word in s_lst:
                if i > len(word) - 1:
                    in_str +=' '
                else: in_str += word[i]  
            ans.append(in_str.rstrip())

        return ans       