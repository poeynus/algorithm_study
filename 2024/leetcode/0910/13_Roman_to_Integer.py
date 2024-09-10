class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }
        i = 0

        while i < len(s):
            if s[i] == "C" or s[i] == "X" or s[i] == "I":
                if i == len(s) - 1:
                    total += roman_dict.get(s[i])
                elif roman_dict.get(s[i] + s[i + 1]) is not None:
                    total += roman_dict.get(s[i] + s[i + 1])
                    i += 1
                else:
                    total += roman_dict.get(s[i])
            else:
                total += roman_dict.get(s[i])

            i += 1
        return total


class OtherSolution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for i, r in enumerate(s):
            if i != len(s) - 1 and roman_dict.get(s[i]) < roman_dict.get(s[i + 1]):
                total -= roman_dict.get(s[i])
            else:
                total += roman_dict.get(s[i])

        print(total)
        return total


OtherSolution().romanToInt("MCMXCIV")

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
