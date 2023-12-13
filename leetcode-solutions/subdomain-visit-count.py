class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        visit_count = {}
        res = []

        for cpdomain in cpdomains:
            count, s = cpdomain.split(' ') 
            count = int(count)
            for i in range(len(s)-1, -1, -1):
                if s[i] == '.':
                    visit_count[s[i+1:]] = visit_count.get(s[i+1:], 0) + count
            visit_count[s] = visit_count.get(s, 0) + count
        for link, count in visit_count.items():
            res.append(str(count) +" "+ str(link))
        return res

        