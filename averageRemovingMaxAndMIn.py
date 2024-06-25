class Solution:
    def average(self, salary: List[int]) -> float:
        # maximun = max(salary)
        # minimum = min(salary)
        # salary.remove(maximun)
        # salary.remove(minimum)
        # sum = 0
        # for sal in salary:
        #     sum += sal
        # return sum/len(salary)
        # sorted1 = sorted(salary)
        # return sum( sorted1[1:-1] ) / (len(salary) -2 )

        salary_sum = sum(salary)
        salary_sum -= max(salary)
        salary_sum -= min(salary)
        return salary_sum / (len(salary)-2)