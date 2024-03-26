from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spacing = [0] + flowerbed + [0]
        for i in range(1, len(spacing) - 1):
            if spacing[i] == 0 and spacing[i + 1] == 0 and spacing[i - 1] == 0:
                n -= 1
                spacing[i] = 1
        if n <= 0:
            return True
        return False

output = Solution()
print(output.canPlaceFlowers([1,0,0,0,1], 1)) # True