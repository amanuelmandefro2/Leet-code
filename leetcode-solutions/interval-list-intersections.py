class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1 = 0
        ptr2 = 0
        ans = []

        while ptr1 < len(firstList) and ptr2 < len(secondList):
            start = max(firstList[ptr1][0], secondList[ptr2][0])
            end = min(firstList[ptr1][1], secondList[ptr2][1])

            if start <= end:
                ans.append([start, end])


            if firstList[ptr1][1] < secondList[ptr2][1]:
                ptr1 += 1
            else:
                ptr2 += 1

        return ans
