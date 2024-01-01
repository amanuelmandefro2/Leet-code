class Solution:
    

    def pancakeSort(self, arr: List[int]) -> List[int]:

        def flip(arr, r):
            l = 0
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        ans = []
        
        for i in range(len(arr)):
            max_val = len(arr)-i
            idx = arr.index(max_val)
            flip(arr, idx)
            flip(arr, max_val - 1)

            ans.append(idx+1)
            ans.append(max_val)

    

        return ans     
            


       