class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        equal_sum = skill[0] + skill[len(skill) - 1]
        chemistry = skill[0]*skill[len(skill) -1]
        l, r = 1, len(skill) - 2
        while l < r:
            if skill[l] + skill[r] != equal_sum:
                return -1
            chemistry += skill[l]*skill[r]
            l += 1
            r -= 1
        return chemistry    

        