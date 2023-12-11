class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        #declearing idx_nums dictionary to add nums idx pair values and answer  
        idx_nums = defaultdict(int)
        answers = []

        #adding values into dictionary
        even_sum = 0
        for i, num in enumerate(nums):
            idx_nums[i] = num
            if num % 2 == 0:
                even_sum += num


        for query in queries:
            val, idx = query
            if idx_nums[idx] % 2 == 0:
                even_sum -= idx_nums[idx]
            
            idx_nums[idx] += val
            if idx_nums[idx] % 2 == 0:
                even_sum += idx_nums[idx]
            answers.append(even_sum)        

       
        return answers    
