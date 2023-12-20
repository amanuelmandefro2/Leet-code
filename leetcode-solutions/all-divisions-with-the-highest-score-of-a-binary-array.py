class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score_i = sum(nums)
        max_score = sum(nums)
        highest_scores = [0]

        for i, value in enumerate(nums, 1):
            if value == 0:
                score_i += 1
            else:
                score_i -= 1
            if score_i > max_score:
                highest_scores = [i]
                max_score = score_i
            elif score_i == max_score:
                highest_scores.append(i)

        return highest_scores                     

        