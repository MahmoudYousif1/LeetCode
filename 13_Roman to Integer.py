class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        specials = {"IV":4, "IX":9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        output = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in specials:
                output += specials[s[i:i+2]]
                i += 2
            else:
                output += numbers[s[i]]
                i += 1
        return(output)

output1 = Solution()
print(output1.romanToInt("III")) #3