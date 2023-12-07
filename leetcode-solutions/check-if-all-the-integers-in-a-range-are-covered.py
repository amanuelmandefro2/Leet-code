class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        range_set = set()

        for r in ranges:
            for num in range(r[0], r[1] +1):
                range_set.add(num)
        
        for num in range(left, right +1):
          if num not in range_set:
            return False
        return True        