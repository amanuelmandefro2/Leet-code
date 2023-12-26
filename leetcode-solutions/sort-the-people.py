class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # pHeightDict = dict()
        # sortedLst = []

        # for i in range(len(names)):
        #     pHeightDict[heights[i]] = names[i]
        # sorted_pHeightDict = sorted( pHeightDict.items(), key=lambda s: s[0], reverse=True)
        # for height, name in sorted_pHeightDict:
        #     sortedLst.append(name)
        # return sortedLst


        # #Bubble sorting 
        # for i in range(len(heights)):
        #     for j in range(len(heights)- i-1):
        #         if heights[j] < heights[j+1]:
        #             names[j], names[j+1] = names[j+1], names[j]
        #             heights[j], heights[j+1] = heights[j+1], heights[j]

        #Selection sorting
        # for i in range(len(heights)-1):
        #     max_idx = i
        #     for j in range(i+1, len(heights)):
        #         if heights[max_idx] < heights[j]:
        #             max_idx = j
        #     if max_idx != i:     
        #         names[i], names[max_idx] = names[max_idx], names[i]  
        #         heights[i], heights[max_idx] = heights[max_idx], heights[i] 
        #insertion sorting
        for i in range(len(heights)-1):
            for j in range(i+1, 0, -1):
                if heights[j] > heights[j-1]:
                    names[j], names[j-1] = names[j-1], names[j]
                    heights[j], heights[j-1] = heights[j-1], heights[j]


                   
        return names            
                