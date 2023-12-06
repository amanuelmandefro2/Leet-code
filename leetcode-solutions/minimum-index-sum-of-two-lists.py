class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = float('inf')
        index_lst = []
        res = []

        for val in list1:
            if val in list2:
                if min_index > list1.index(val)+ list2.index(val):
                    res = [val]
                elif min_index == list1.index(val)+ list2.index(val):
                    res.append(val)    
                min_index = min(min_index, list1.index(val)+ list2.index(val))
        return res        

      

        