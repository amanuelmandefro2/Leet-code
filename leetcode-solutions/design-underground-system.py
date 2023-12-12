class UndergroundSystem:

    def __init__(self):
        #declear the start dictionary to store id to start station or check station of the given person
        #and time_finish to store check in and check out station as key and the time of every person
        #check in as value and it is list
        self.start = {}
        self.time_finish = defaultdict(list)
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.time_finish[(self.start[id][0], stationName)].append(t - self.start[id][1])  

    def getAverageTime(self, startStation: str, endStation: str) -> float:
      
        return sum(self.time_finish[startStation, endStation])/len(self.time_finish[startStation, endStation])
        

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)