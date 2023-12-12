class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = {}
        self.ptr = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:


        self.stream[idKey] = [value]

        ans = []

        while self.ptr <= self.n and  self.ptr in self.stream :
            ans += self.stream[self.ptr]
            self.ptr += 1

        return ans   

        # else:
        #     if stream[idkey - 1]:
        #         return stream[idKey]
        #     elif stream[idKey + 1]:
        #         return         
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)