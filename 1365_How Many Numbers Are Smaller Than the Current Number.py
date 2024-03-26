from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            total = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    total += 1
            output.append(total)
        return output

output = Solution()
print(output.smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]