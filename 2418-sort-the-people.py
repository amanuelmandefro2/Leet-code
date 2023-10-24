class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pHeightDict = dict()
        sortedLst = []
        for i in range(len(names)):
            pHeightDict[heights[i]] = names[i]
        sorted_pHeightDict = sorted( pHeightDict.items(), key=lambda s: s[0], reverse=True)
        for height, name in sorted_pHeightDict:
            sortedLst.append(name)
        return sortedLst
