class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        start_decreasing = False   

        i = 1
        if arr[0] > arr[1]:
            return False
        while i < len(arr) and not start_decreasing:
            if arr[i-1] == arr[i]:
                return False
            if arr[i-1] > arr[i]:
                start_decreasing = True
            i += 1
        while  i < len(arr) and start_decreasing:
            if arr[i-1] <= arr[i]:
                return False
            i += 1
        return start_decreasing                


        