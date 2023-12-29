class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s_lst = ['']*len(s)

        for word in s:
            idx = int(word[-1]) -1
            s_lst[idx] = word[:len(word)-1]

        return ' '.join(s_lst)    