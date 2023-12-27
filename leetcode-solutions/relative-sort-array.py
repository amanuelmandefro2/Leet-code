class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for ord in arr2:
            for num in arr1:
                if num == ord:
                    ans.append(num)
        not_ord = []
        ans_set = set(ans)
        for num in arr1:
            if num not in ans_set:
                not_ord.append(num)             

        
        not_ord.sort()
        ans = ans + not_ord[0:]
        return ans           

        