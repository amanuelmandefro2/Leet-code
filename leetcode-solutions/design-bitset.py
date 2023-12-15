class Bitset:

    def __init__(self, size: int):
        self.size = size

        self.zero_counter = self.size
        self.one_counter = 0

        self.bits = ['0']*self.size
        self.flip_bits = ['1']*self.size
        

    def fix(self, idx: int) -> None:
        
        if self.zero_counter >= 1 and self.bits[idx] == '0':
            self.zero_counter -= 1
            self.one_counter += 1 
             
        self.bits[idx] = '1' 
        self.flip_bits[idx] = '0'
        
        

    def unfix(self, idx: int) -> None:
        if self.one_counter >= 1 and self.bits[idx] == '1':
            self.zero_counter += 1
            self.one_counter -= 1

        self.bits[idx] = '0' 
        self.flip_bits[idx] = '1'

     
  
        

    def flip(self) -> None:
        self.zero_counter, self.one_counter = self.one_counter, self.zero_counter
        self.bits, self.flip_bits = self.flip_bits, self.bits


        

    def all(self) -> bool:
        return self.one_counter == self.size
        

    def one(self) -> bool:
        return self.one_counter >= 1
        

    def count(self) -> int:
        return self.one_counter
        

    def toString(self) -> str:
        return (''.join(self.bits))
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()