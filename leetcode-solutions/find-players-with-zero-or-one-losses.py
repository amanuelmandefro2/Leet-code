class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        matches_loss = {}
        less_loss = [set(), set()]

        for match in matches:
            matches_loss[match[1]] = matches_loss.get(match[1], 0) + 1

        for match in matches:
            if match[0] not in matches_loss :
                less_loss[0].add(match[0])
            elif matches_loss[match[0]] == 1:
                less_loss[1].add(match[0])
            if match[1] not in matches_loss:
                less_loss[0].add(match[1])
            elif matches_loss[match[1]] == 1:
                less_loss[1].add(match[1])

        less_loss[0] = list(less_loss[0])
        less_loss[1] = list(less_loss[1])
        
        less_loss[0].sort()
        less_loss[1].sort()

        return less_loss
