class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if strs[0] == '':
            return ''


        for i in range(len(strs[0])):
            notFound = False
            for j in range(1, len(strs)):
                if len(strs[j]) > i:
                    if strs[j][i] != strs[0][i]:
                        notFound = True
                        break
                else:
                    notFound = True
            if notFound:
                break
            res += strs[0][i]

        return res
        
        