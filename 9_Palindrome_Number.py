class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

output = Solution()
print(output.isPalindrome(10))