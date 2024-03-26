from ast import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        output = 0
        for chars in strs:
            try:
                if int(chars) > output:
                    output = int(chars)
            except ValueError:
                if len(chars) > output:
                    output = len(chars)
        return output

output = Solution()
print(output.maximumValue(["1","2","3","4","5","6","7","8","9","10"])) # 10