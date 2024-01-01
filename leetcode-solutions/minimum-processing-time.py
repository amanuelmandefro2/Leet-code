class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        j = 0
        min_time = -float('inf')
        for i in range(0, len(tasks)-3, 4):
           time_p = max(processorTime[j]+tasks[i], processorTime[j]+tasks[i+1], 
           processorTime[j]+tasks[i+2], processorTime[j]+tasks[i+3])
           min_time = max(min_time, time_p)
           j += 1

        return min_time   
            
        