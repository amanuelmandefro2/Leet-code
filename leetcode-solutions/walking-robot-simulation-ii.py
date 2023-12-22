class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.position = [0, 0]
        self.direction = 'East'
        

    def step(self, num: int) -> None:
        i = 0
        p = 2*(self.height + self.width) - 4
        num =  num % p
        while i < num:
            j = i
            while j < num and self.direction == 'East':
                self.position[0] += 1
                j += 1 
                if self.position[0] == self.width:
                    self.direction = 'North'
                    self.position[0] -= 1
                    j -= 1
                   
            while j < num and self.direction == 'North':
                self.position[1] += 1
                j += 1
                print(*self.position )
                print(self.height)
                if self.position[1] == self.height:
                    self.direction = 'West'  
                    self.position[1] -= 1
                    j -= 1
                
            while j < num and self.direction == 'West':
                self.position[0] -= 1
                j += 1
                if self.position[0] < 0:
                    self.direction = 'South'
                    self.position[0] = 0
                    j -= 1

               
            while j < num and self.direction == 'South':
                self.position[1] -= 1
                j += 1
                if self.position[1] < 0 :
                    self.direction = 'East'
                    self.position[1] = 0  
                    j -=  1
                    
                 
            i = j                  

        if self.position == [0, 0]:
            self.direction = 'South'       
        

    def getPos(self) -> List[int]:
        return self.position
        

    def getDir(self) -> str:
        return self.direction
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()