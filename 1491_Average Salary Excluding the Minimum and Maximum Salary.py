from ast import List

class Solution:
    def average(self, salary: List[int]) -> float:
        getmin = min(salary)
        getmax = max(salary)

        salary.remove(getmin)
        salary.remove(getmax)
        total = sum(salary)/ len(salary)
        return total

output = Solution()
print(output.average([4000,3000,1000,2000])) # 2500.00000