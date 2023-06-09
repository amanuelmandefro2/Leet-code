#User function Template for python3

class Solution: 
    def select(self, arr, i):
        return arr[i]  
    
    def selectionSort(self, arr,n):
        
        for i in range(n):
            min_index = i
            select_elem = self.select(arr, i)
            for j in range(i+1, n):
                if select_elem > arr[j]:
                    select_elem = arr[j]
                    min_index = j
            arr[min_index] = arr[i]
            arr[i] = select_elem
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends