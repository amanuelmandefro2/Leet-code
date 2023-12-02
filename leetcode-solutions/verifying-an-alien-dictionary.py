class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for i in range(len(words)-1):
            j = 0
            first, second = words[i], words[i+1]
            while len(first) > j and len(second)  > j and first[j] == second[j]:
                    j += 1
            
            if len(first) > len(second) and (len(second) <= j):
                return False
            if len(words[i]) > j and len(words[i+1])  > j and order.index(words[i][j ]) > order.index(words[i +1][j]):
                return False
        return True

        