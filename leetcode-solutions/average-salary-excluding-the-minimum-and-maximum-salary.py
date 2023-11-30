class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)

        sum_salary = 0

        for sal in salary:
            if sal == min_salary or sal == max_salary:
                continue
            sum_salary += sal

        return sum_salary/(len(salary)-2)
        