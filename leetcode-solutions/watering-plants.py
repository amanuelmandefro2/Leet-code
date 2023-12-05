class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        steps = 0
        i = 0
        while i < len(plants):
            if plants[i] <= cap:
                cap -= plants[i]
                plants[i] = 0
                steps += 1
            j = i   
            while cap < plants[j] and i > -1:
                if i == j:
                    i -= 1
                steps += 1
                i -= 1
            if i == -1:
                cap  = capacity
                        
            i += 1    

        return  steps    
                


        