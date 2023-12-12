class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        good_int = float('inf')

        both_found = []

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                both_found.append(fronts[i])

        for i in range(len(fronts)):
            if fronts[i] not in both_found:
                good_int = min(fronts[i], good_int)
            if backs[i] not in both_found:
                good_int = min(backs[i], good_int)   


        return 0 if good_int == float('inf') else good_int   
        