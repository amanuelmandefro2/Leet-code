class FrequencyTracker(object):

    def __init__(self):
        self.Dict = defaultdict(int)
        self.fdict = defaultdict(int)
        
    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
                

        self.fdict[self.Dict[number]] = max(0, self.fdict[self.Dict[number]] - 1)    
        self.Dict[number]+=1
        self.fdict[self.Dict[number]]+=1
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """

        self.fdict[self.Dict[number]]  = max(0, self.fdict[self.Dict[number]] - 1)
        self.Dict[number] = max(0, self.Dict[number] - 1)  
        self.fdict[self.Dict[number]] += 1    

        

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        return self.fdict[frequency] != 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)