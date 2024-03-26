from ast import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        output = 0
        h1 = heights
        h2 = sorted(heights)
        for i in range(len(h2)):
            if h1[i] != h2[i]:
                output += 1
        return output

output = Solution()
print(output.heightChecker([1,1,4,2,1,3])) #3