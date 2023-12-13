class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.token = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token and currentTime < self.token[tokenId] + self.timeToLive:
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        unexpired_token = 0
        for key in self.token:
            if self.token[key] + self.timeToLive > currentTime:
                unexpired_token += 1 
        return unexpired_token
      

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)